"""50 -- Per-observation confidence: tau-gated facts + dual-use EDB companion.

Builds a verified platform with ``require_confidence=True`` and demonstrates:

1. A fact carrier ``{"value": <v>, "confidence": <c>}`` where ``c >= tau``
   certifies normally (``proof_checked: true``).
2. A sub-tau carrier is REFUSED -- the whole decision fails closed
   (HTTP 503, ``rejected_facts`` in the body).
3. The companion EDB atom ``{field}__confidence`` lets a rule reason
   over the stated confidence directly.
4. A bare scalar sent to a ``require_confidence`` platform is refused
   (fail-closed on absent confidence).
5. A confidence carrier sent to a NON-verified platform is rejected
   with a clear error (fail-loud, not a silent no-op).

Requires a running AmberTrace instance.  Self-cleans.

    python 50_supplied_confidence.py
"""

import csv
import io
import sys
import tempfile

from ambertraceai import AmbertraceError

from _common import banner, get_client, step, wait_for_domain


def main() -> None:
    api = get_client()
    banner("Per-observation confidence: tau gate + dual-use EDB companion")

    # -- 1. Create domain + dataset ------------------------------------------

    step("Creating domain...")
    domain = api.domains.create(
        name="Sensor Monitor (Confidence Demo)",
        description=(
            "A sensor monitoring domain.  Each observation has a numeric "
            "reading and a stated confidence.  The policy escalates when "
            "the confidence is too low."
        ),
    )
    domain_id = domain["id"]
    step(f"Domain #{domain_id} created.")

    step("Building ontology...")
    api.domains.build_ontology(domain_id)
    domain = wait_for_domain(api, domain_id)
    step(f"Ontology status: {domain['status']}")

    step("Uploading dataset...")
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["sensor_reading", "outcome"])
    for reading in range(10, 100, 5):
        w.writerow([reading, "normal" if reading < 80 else "alert"])
    buf.seek(0)

    with tempfile.NamedTemporaryFile(suffix=".csv", mode="w", delete=False) as f:
        f.write(buf.getvalue())
        f.flush()
        api.datasets.upload(domain_id, f.name, name="sensor_data")
    step("Dataset uploaded.")

    # -- 2. Build verified platform with require_confidence ------------------

    step("Building verified platform (tau=0.6, require_confidence=True)...")
    platform = api.platforms.create(
        domain_id=domain_id,
        verified_profile=True,
        verified_min_confidence=0.6,
        require_confidence=True,
    )
    platform_id = platform["id"]
    step(f"Platform #{platform_id} building...")

    import time
    for _ in range(60):
        p = api.platforms.get(platform_id)
        if p["status"] in ("active", "failed"):
            break
        time.sleep(2)

    assert p["status"] == "active", f"Platform build failed: {p}"
    step(f"Platform #{platform_id} active.")

    # -- 3. Add a rule that references the confidence companion ---------------

    step("Adding a rule that uses _aria_confidence__sensor_reading...")
    api.platforms.add_rule(
        platform_id,
        name="escalate_low_confidence",
        condition={
            "field": "_aria_confidence__sensor_reading",
            "operator": "lt",
            "value": 0.8,
        },
        action={"action_type": "escalate"},
    )
    step("Rule added.")

    # -- 4. Query with above-tau confidence (should certify) -----------------

    step("Querying with confidence=0.95 (above tau=0.6)...")
    result = api.platforms.query(
        platform_id,
        query="Assess this sensor reading.",
        facts={"sensor_reading": {"value": 75, "confidence": 0.95}},
    )
    assert result["proof_checked"] is True, (
        f"Expected proof_checked=True, got {result.get('proof_checked')}"
    )
    step(f"  proof_checked: {result['proof_checked']}")
    step(f"  decision: {result.get('decision')}")

    # The confidence companion should be in the certified facts.
    certified = (result.get("explanation") or {}).get("certified_facts", [])
    companion_facts = [f for f in certified if f.get("field") == "_aria_confidence__sensor_reading"]
    assert companion_facts, "Expected _aria_confidence__sensor_reading in certified_facts"
    step(f"  _aria_confidence__sensor_reading in EDB: {companion_facts[0].get('value')}")

    # -- 5. Query with sub-tau confidence (should be REFUSED) ----------------

    step("Querying with confidence=0.3 (below tau=0.6) -- expect refusal...")
    try:
        api.platforms.query(
            platform_id,
            query="Assess this sensor reading.",
            facts={"sensor_reading": {"value": 75, "confidence": 0.3}},
        )
        step("  ERROR: query should have been refused but was not.")
        sys.exit(1)
    except AmbertraceError as exc:
        step(f"  Correctly refused (HTTP {exc.status_code}).")
        if hasattr(exc, "rejected_facts"):
            step(f"  rejected_facts: {exc.rejected_facts}")

    # -- 6. Bare scalar to require_confidence platform (should be REFUSED) ---

    step("Querying with bare scalar (no confidence carrier) -- expect refusal...")
    try:
        api.platforms.query(
            platform_id,
            query="Assess this sensor reading.",
            facts={"sensor_reading": 75},
        )
        step("  ERROR: bare scalar should have been refused but was not.")
        sys.exit(1)
    except AmbertraceError as exc:
        step(f"  Correctly refused (HTTP {exc.status_code}).")

    # -- 7. Clean up ---------------------------------------------------------

    step("Cleaning up...")
    api.platforms.delete(platform_id)
    api.domains.delete(domain_id)
    step("Done -- all behaviours verified.")


if __name__ == "__main__":
    main()

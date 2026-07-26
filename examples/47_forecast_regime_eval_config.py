"""47 — Forecast / Regime Eval Config (``direction="separate"``).

An **eval config** names the ONE domain-level outcome metric that rule
suggestion and rule discovery are scored against. For most domains the metric
has a fixed direction — minimise readmissions, maximise ROI. A **forecast or
regime** domain does not: the useful question is not "does this rule push the
number up" but "does this rule's FIRING predict what happens NEXT".

That is what ``direction="separate"`` is for. The target metric is a
FORWARD-LOOKING column in your own data (here ``regime_persists_next_month``,
a 0/1 flag for "next month's curve regime matches this month's"), and a rule
passes the evaluation gate when its firing **predictively separates** that
column — a signed effect either way, scored by effect size. Two consequences:

- ``calculation`` may be OMITTED. Because the target IS a data column, it
  auto-defaults to the mean of that column — a declarative record of how the
  metric is derived from your data, stored alongside the config.
- Without ``separate``, a forecast rule has no honest direction to be scored
  on and the evaluation gate silently SKIPS it.

This demo also shows the rejection path. Every enumerated field (``direction``,
``unit``, ``calculation.type``, ``calculation.aggregate``) is rejected with a
422 that NAMES the offending field and lists the permitted values, so you read
the error instead of guessing. Where the rejection comes from the server-side
validator it also carries a structured ``error.details`` entry
(``AmbertraceError.details``); a request-schema rejection carries the same
information as prose on the message.

Creates resources on your account. Run with --help for options.

    python 47_forecast_regime_eval_config.py
"""

from __future__ import annotations

import argparse
import csv
import random
import re
import tempfile
from pathlib import Path

from ambertraceai import AmbertraceError

from _common import (
    add_common_args,
    build_ontology,
    print_dataset,
    print_ontology,
    print_section,
    run_demo,
)

DOMAIN_NAME = "UK Curve Regime Persistence"
DOMAIN_DESCRIPTION = (
    "Monthly UK government-bond curve regimes and whether the regime persists "
    "into the following month. Each row is one month with the 2y and 10y yields, "
    "the 10y-2y slope, the realised volatility, the regime label for that month, "
    "and regime_persists_next_month — a forward-looking 0/1 flag that is 1 when "
    "next month's regime equals this month's. Rules are judged on whether their "
    "firing predicts regime persistence."
)

# The forward-looking column the eval config targets.
TARGET_METRIC = "regime_persists_next_month"


def _write_panel(path: Path, n_months: int = 96, seed: int = 7) -> Path:
    """Write a small monthly curve-regime panel with a forward outcome column."""
    rng = random.Random(seed)
    rows = []
    slope = 0.6
    for i in range(n_months):
        slope = round(max(-1.5, min(2.0, slope + rng.gauss(0, 0.18))), 3)
        vol = round(abs(rng.gauss(0.55, 0.20)), 3)
        y2 = round(3.5 + rng.gauss(0, 0.35), 3)
        rows.append({
            "month": f"{2018 + i // 12}-{i % 12 + 1:02d}",
            "yield_2y": y2,
            "yield_10y": round(y2 + slope, 3),
            "slope_10y_2y": slope,
            "realised_vol": vol,
            "regime": "steepening" if slope > 0.4 else (
                "flat" if slope > -0.1 else "inverted"),
        })
    # The forward flag: does NEXT month's regime match THIS month's?
    for i, row in enumerate(rows[:-1]):
        row["regime_persists_next_month"] = int(rows[i + 1]["regime"] == row["regime"])
    rows = rows[:-1]  # the last month has no next month — drop it

    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def _rejection_summary(exc: AmbertraceError) -> str:
    """The useful part of a 422: the offending field + the permitted values.

    A server-side validation rejection carries structured ``details``
    (``field`` + a curated message), so use those directly. A request-schema
    rejection arrives as prose instead — keep only the lines carrying the field
    name and the permitted values, and drop the framework's own header and
    doc-URL lines, which tell a caller nothing about their config.
    """
    if exc.details:
        return "; ".join(
            f"{d.get('field')}: {d.get('message')}" for d in exc.details)
    keep = []
    for raw in (exc.message or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("For further information"):
            continue
        if "validation error" in line and " for " in line:
            continue
        keep.append(re.sub(r"\s*\[type=.*\]$", "", line))
    return " -> ".join(keep) if keep else f"rejected with HTTP {exc.status_code}"


def _show_rejection(api, domain_id: int, label: str, **kwargs) -> None:
    """Attempt a deliberately invalid config and print what the API tells us."""
    try:
        api.domains.set_eval_config(domain_id, **kwargs)
        print(f"  {label}: unexpectedly ACCEPTED")
    except AmbertraceError as exc:
        print(f"  {label}: rejected -> {_rejection_summary(exc)}")


def run_forecast_eval_config(api, args: argparse.Namespace) -> None:
    total = 6

    with tempfile.TemporaryDirectory() as tmp:
        dataset_path = args.dataset or _write_panel(
            Path(tmp) / "uk_curve_regimes.csv")

        print_section(1, total, "Creating the curve-regime domain")
        domain = api.domains.create(name=DOMAIN_NAME, description=DOMAIN_DESCRIPTION)
        print(f"  Domain {domain['id']}: {domain['name']} ({domain.get('status')})")

        print_section(2, total, "Uploading the monthly panel")
        dataset = api.datasets.upload(domain_id=domain["id"], file_path=str(dataset_path))
        print_dataset(dataset)

    print_section(3, total, "Building the ontology")
    domain = build_ontology(api, domain["id"])
    print_ontology(domain, limit=10)

    print_section(4, total, "Setting the forecast/regime eval config")
    # The whole point: direction="separate" + a forward-looking target column.
    # No 'calculation' block — it auto-defaults to the mean of the target column.
    config = api.domains.set_eval_config(
        domain["id"],
        target_metric=TARGET_METRIC,
        direction="separate",
        unit="rate",
        description="Does next month's curve regime match this month's?",
        significance_threshold_pp=1.0,
        min_positive_fraction=0.6,
    )
    print(f"  target_metric: {config['target_metric']}")
    print(f"  direction:     {config['direction']}")
    print(f"  unit:          {config['unit']}")
    print(f"  calculation:   {config['calculation']}   <- auto-defaulted")

    print_section(5, total, "Reading it back")
    stored = api.domains.eval_config(domain["id"])
    assert stored["direction"] == "separate", stored
    print(f"  stored: {stored}")

    print_section(6, total, "What a rejection looks like (each names the field)")
    _show_rejection(
        api, domain["id"], "unit='furlongs'",
        target_metric=TARGET_METRIC, direction="separate", unit="furlongs",
    )
    _show_rejection(
        api, domain["id"], "direction='sideways'",
        target_metric=TARGET_METRIC, direction="sideways",
    )
    _show_rejection(
        api, domain["id"], "calculation.type='custom' without notes",
        target_metric=TARGET_METRIC, direction="maximize",
        calculation={"type": "custom"},
    )

    print(f"\nDone. Domain {domain['id']} carries a forecast/regime eval config; "
          "rule suggestions on this domain are now scored on whether their firing "
          f"predicts {TARGET_METRIC}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Forecast/regime eval config — AmberTrace AI demo",
    )
    add_common_args(parser)
    parser.add_argument(
        "--dataset", type=Path, default=None,
        help="CSV to upload (default: a generated monthly curve-regime panel)",
    )
    args = parser.parse_args()
    run_demo(run_forecast_eval_config, args)


if __name__ == "__main__":
    main()

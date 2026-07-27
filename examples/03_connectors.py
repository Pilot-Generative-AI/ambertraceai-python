"""03 -- Connectors: discover and filter external data sources.

Lists the available data-source connectors with their config requirements and
taxonomy metadata (asset classes, countries, currencies). Supports filtering
by ``asset_class``, ``country``, and ``currency`` query parameters.

Connectors that hit third-party providers (e.g. FRED) need *your own* provider
API key, supplied in the ``config`` dict. Read-only -- creates nothing.

    python 03_connectors.py
"""

from _common import banner, get_client, step
from ambertraceai import AmbertraceError


def main() -> None:
    api = get_client()
    banner("Connectors -- discovery and filtering")

    # --- 1. List all connectors with taxonomy metadata ----------------------
    connectors = api.connectors.list()
    step(f"{len(connectors)} connector(s) available:")
    for c in connectors:
        ctype = c.get("type") or c.get("name")
        requires = c.get("requires") or []
        classes = c.get("asset_classes") or []
        countries = c.get("countries") or []
        currencies = c.get("currencies") or []
        desc = c.get("description", "")
        print(f"      {ctype}: {desc}")
        print(f"        requires: {requires}")
        print(f"        asset_classes: {classes}  countries: {countries}  currencies: {currencies}")
        print(f"        redistributable: {c.get('redistributable')}  entitlement: {c.get('entitlement')}")

    # --- 2. Filter by asset class -------------------------------------------
    step("Filtering connectors by asset_class='rates'...")
    rates = api.connectors.list(asset_class="rates")
    step(f"  {len(rates)} rate connector(s): {[c['type'] for c in rates]}")

    # --- 3. Filter by country -----------------------------------------------
    step("Filtering connectors by country='GB'...")
    gb = api.connectors.list(country="GB")
    step(f"  {len(gb)} GB connector(s): {[c['type'] for c in gb]}")

    # --- 4. Filter by currency ----------------------------------------------
    step("Filtering connectors by currency='EUR'...")
    eur = api.connectors.list(currency="EUR")
    step(f"  {len(eur)} EUR connector(s): {[c['type'] for c in eur]}")

    # --- 5. Combined filter -------------------------------------------------
    step("Filtering connectors by asset_class='rates', country='GB', currency='GBP'...")
    gb_rates = api.connectors.list(asset_class="rates", country="GB", currency="GBP")
    step(f"  {len(gb_rates)} GB rates connector(s): {[c['type'] for c in gb_rates]}")

    # --- 6. Test a connector (optional) -------------------------------------
    if connectors:
        sample = connectors[0]
        ctype = sample.get("type") or sample.get("name")
        step(f"Attempting a config test for '{ctype}' (may require provider keys)...")
        try:
            result = api.connectors.test(connector_type=ctype, config={})
            step(f"Test result: rows={result.get('rows')} columns={result.get('columns')}")
        except AmbertraceError as e:
            step(f"Test rejected ({e.code}): {e}  -- expected without provider config.")

    # --- 7. validate_only: check a config WITHOUT fetching -------------------
    # An ASYNC connector (one that fetches in the background) cannot be tested
    # inline -- a plain test() returns 422.  validate_only=True checks the
    # config only, and works for every connector including the async ones.
    step("Validating an async connector's config with validate_only=True...")
    check = api.connectors.test(
        connector_type="boe_yield_curves",
        config={"curve_types": ["nominal"], "max_backfill_archives": 2},
        validate_only=True,
    )
    step(f"  valid={check.get('valid')} errors={check.get('errors')}")

    # The same call with a bad config reports WHY, without any network fetch.
    bad = api.connectors.test(
        connector_type="boe_yield_curves",
        config={"curve_types": ["not_a_curve"]},
        validate_only=True,
    )
    step(f"  bad config -> valid={bad.get('valid')} errors={bad.get('errors')}")

    print("\nConnector discovery complete.")


if __name__ == "__main__":
    main()

"""62 -- UK CPI/COICOP inflation data from the ONS connector.

Demonstrates the ``ons`` connector: fetch UK CPI data from the Office for
National Statistics (ONS) timeseries API at COICOP division granularity,
including expenditure weights and contribution series.

The ONS connector delivers:

  * **CPI/CPIH indices and annual rates** -- headline, core, goods/services
    split, all 12 COICOP divisions, and special-aggregate exclusion measures
    (ex-energy, ex-energy-and-unprocessed-food, core ex-energy-food-alcohol-
    tobacco).
  * **Expenditure weights** -- annual per-division weights (parts per 1000),
    the building blocks for weighted-mean/trimmed-mean inflation measures.
  * **Contribution series** -- the contribution of each COICOP division to
    the all-items annual rate (CDIDs WUMA--WUNG).
  * **Vintage tracking** -- CPI data is subject to revision; the connector
    stores per-(CDID, date) revision lists via the ConnectorArchive, giving
    genuine as-of vintage reconstruction for honest backtests.

All data is published under the UK Open Government Licence v3.0 (OGL) --
free reuse, including commercial, with attribution.

Prerequisites:
    * ``AMBERTRACE_API_KEY`` -- your Ambertrace API key (see examples/.env).
    * No additional API key required -- the ONS timeseries endpoint is public.

    python 62_uk_cpi_ons_connector.py [--domain-id N]
"""

from __future__ import annotations

import sys

from _common import banner, get_client, step


def main() -> None:
    banner("62 -- UK CPI/COICOP inflation data from the ONS connector")
    api = get_client()

    domain_id = None
    for arg in sys.argv[1:]:
        if arg.startswith("--domain-id"):
            domain_id = int(arg.split("=")[1] if "=" in arg else sys.argv[sys.argv.index(arg) + 1])

    # ----------------------------------------------------------------
    # Step 1: Fetch the CPI all-items index + annual rate
    # ----------------------------------------------------------------
    step("1. Fetch CPI headline series (D7BT index, D7G7 annual rate)")
    result = api.datasets.fetch(
        connector_type="ons",
        config={
            "series": ["D7BT", "D7G7"],
            "dataset": "MM23",
            "frequency": "monthly",
            "start_date": "2020-01-01",
        },
        domain_id=domain_id,
    )
    print(f"  Status: {result.status}")
    print(f"  Rows:   {result.row_count}")
    print(f"  Cols:   {result.columns}")
    if result.row_count and result.row_count > 0:
        print("  (Headline CPI index + annual rate fetched successfully)")

    # ----------------------------------------------------------------
    # Step 2: Fetch all 12 COICOP division indices + weights
    # ----------------------------------------------------------------
    step("2. Fetch COICOP division indices (01-12) + expenditure weights")

    # Division index CDIDs and weight CDIDs.
    division_indices = [
        "D7BU",  # 01 food and non-alcoholic beverages
        "D7BV",  # 02 alcoholic beverages, tobacco and narcotics
        "D7BW",  # 03 clothing and footwear
        "D7BX",  # 04 housing, water and fuels
        "D7BY",  # 05 furniture, household equipment
        "D7BZ",  # 06 health
        "D7C2",  # 07 transport
        "D7C3",  # 08 communication
        "D7C4",  # 09 recreation and culture
        "D7C5",  # 10 education
        "D7C6",  # 11 restaurants and hotels
        "D7C7",  # 12 miscellaneous goods and services
    ]

    result = api.datasets.fetch(
        connector_type="ons",
        config={
            "series": division_indices,
            "dataset": "MM23",
            "frequency": "monthly",
            "start_date": "2020-01-01",
        },
        domain_id=domain_id,
    )
    print(f"  Status: {result.status}")
    print(f"  Rows:   {result.row_count}")
    print(f"  Series: {len(result.columns) - 1} COICOP divisions")

    # ----------------------------------------------------------------
    # Step 3: Fetch expenditure weights (annual frequency)
    # ----------------------------------------------------------------
    step("3. Fetch expenditure weights (annual, parts per 1000)")

    weight_cdids = [
        "CHZQ",  # 00 all items (= 1000 by construction)
        "CHZR",  # 01 food
        "CHZS",  # 02 alcohol/tobacco
        "CHZT",  # 03 clothing
        "CHZU",  # 04 housing
        "CHZV",  # 05 furniture
        "CHZW",  # 06 health
        "CHZX",  # 07 transport
        "CHZY",  # 08 communication
        "CHZZ",  # 09 recreation
        "CJUU",  # 10 education
        "CJUV",  # 11 restaurants/hotels
        "CJUW",  # 12 miscellaneous
    ]

    result = api.datasets.fetch(
        connector_type="ons",
        config={
            "series": weight_cdids,
            "dataset": "MM23",
            "frequency": "annual",
        },
        domain_id=domain_id,
    )
    print(f"  Status: {result.status}")
    print(f"  Rows:   {result.row_count} (one per year)")
    print(f"  Series: {len(result.columns) - 1} weight CDIDs")

    # ----------------------------------------------------------------
    # Step 4: Fetch contribution series (WUMA-WUNG)
    # ----------------------------------------------------------------
    step("4. Fetch division contributions to the all-items annual rate")

    contribution_cdids = [
        "WUMA",  # 01 food
        "WUMB",  # 02 alcohol/tobacco
        "WUMC",  # 03 clothing
        "WUMD",  # 04 housing
        "WUMP",  # 05 furniture
        "WUMQ",  # 06 health
        "WUMW",  # 07 transport
        "WUMX",  # 08 communication
        "WUNC",  # 09 recreation
        "WUND",  # 10 education
        "WUNE",  # 11 restaurants/hotels
        "WUNG",  # 12 miscellaneous
    ]

    result = api.datasets.fetch(
        connector_type="ons",
        config={
            "series": contribution_cdids,
            "dataset": "MM23",
            "frequency": "monthly",
            "start_date": "2020-01-01",
        },
        domain_id=domain_id,
    )
    print(f"  Status: {result.status}")
    print(f"  Rows:   {result.row_count}")
    print(f"  Series: {len(result.columns) - 1} contribution series")

    # ----------------------------------------------------------------
    # Step 5: Discover ONS series via the data search API
    # ----------------------------------------------------------------
    step("5. Discover ONS CPI series via /data/search")

    search = api.data.search(q="UK inflation", limit=10)
    ons_hits = [
        h for h in search.items
        if getattr(h, "connector_type", None) == "ons"
    ]
    print(f"  ONS hits for 'UK inflation': {len(ons_hits)} (of {search.total} total)")
    for h in ons_hits[:5]:
        print(f"    {h.name}: {h.description[:80]}...")

    print("\n  Done. All data sourced under OGL v3.0 -- attribution: "
          "Source: ONS, Open Government Licence v3.0.")


if __name__ == "__main__":
    main()

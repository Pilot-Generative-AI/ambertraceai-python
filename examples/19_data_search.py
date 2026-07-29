"""19 -- Data Search: resolve NL data requests to concrete series.

Demonstrates the agent workflow for the instruction:

    'build me a model of 5y german rate, using economic data,
     asian equities, developed-market FX'

Each clause maps to a structured search call via
``api.connectors.search(...)``:

  (a) '5y german rate'       -> asset_class=rates, region=eurozone, tenor=5Y
      NOTE: euro-area sovereign yield curves are tagged country='EA', not
      'DE' -- use region='eurozone' (which includes EA) instead of
      country='DE' to find German/euro-area rates.
  (b) 'economic data'        -> asset_class=economics/macro
  (c) 'asian equities'       -> asset_class=equities, region=asia
  (c2) equity coverage       -> asset_class=equities, region=europe
       NOTE: the redistributable equity SERIES are the OECD broad
       share-price indices on FRED (SPASTT01EZM661N euro area,
       SPASTT01GBM661N UK, SPASTT01USM661N US) -- monthly broad-market
       PROXIES (2015=100), NOT the tradeable indices.
  (d) 'developed-market FX'  -> asset_class=fx, region=developed-markets
  (e) 'UK inflation'         -> q='UK inflation' (or country='GB')

Supported filters:
  - Structured: asset_class, country, region, currency, tenor
  - Free-text (q=): lexical substring match on names/descriptions
  - Region groups: asia, europe, americas, developed-markets,
    emerging-markets, G7, G10, eurozone
  - Pagination: offset, limit

Results include both connector-level and series-level entries.
Series-level entries cover the statically-enumerable set (ECB yield
curves, BoE gilts, FRED DGS rates, common macro indicators, the FRED
OECD broad share-price proxies for the euro area/UK/US, and the curated
ONS UK CPI catalog -- 62 MM23 CDIDs covering the headline and core
measures, the 12 COICOP division indices and annual rates, their annual
expenditure weights and their contributions to the all-items rate).

    python 19_data_search.py
"""

from _common import banner, get_client, step


def main() -> None:
    api = get_client()
    banner("Data Search -- agent-driven data resolution")

    # (a) 5Y German rate -> eurozone rates with 5Y tenor.
    # Euro-area curves are tagged EA (not DE), so region=eurozone is the
    # correct decomposition -- country=DE would return empty.
    step("(a) Resolve '5y german rate'")
    resp_a = api.connectors.search(
        asset_class="rates", region="eurozone", tenor="5Y",
    )
    print(f"  Found {resp_a['pagination']['total']} results")
    for item in resp_a["data"][:3]:
        print(f"    [{item['level']}] {item['connector_type']}/{item['name']}: {item['description']}")

    # (b) Economic data
    step("(b) Resolve 'economic data'")
    resp_b = api.connectors.search(asset_class="economics/macro")
    print(f"  Found {resp_b['pagination']['total']} results")
    connectors = {item["connector_type"] for item in resp_b["data"]}
    print(f"  Connector types: {sorted(connectors)}")

    # (c) Asian equities
    step("(c) Resolve 'asian equities'")
    resp_c = api.connectors.search(asset_class="equities", region="asia")
    print(f"  Found {resp_c['pagination']['total']} results")
    for item in resp_c["data"]:
        print(f"    [{item['level']}] {item['connector_type']}: {item['description']}")

    # (c2) Equity coverage: the redistributable OECD share-price proxies.
    step("(c2) Resolve equity coverage to redistributable series")
    resp_c2 = api.connectors.search(asset_class="equities", region="europe")
    print(f"  Found {resp_c2['pagination']['total']} results")
    for item in resp_c2["data"]:
        if item["level"] == "series":
            print(f"    {item['connector_type']}/{item['name']} "
                  f"({','.join(item['countries'])}): {item['description']}")

    # (d) Developed-market FX
    step("(d) Resolve 'developed-market FX'")
    resp_d = api.connectors.search(asset_class="fx", region="developed-markets")
    print(f"  Found {resp_d['pagination']['total']} results")
    for item in resp_d["data"]:
        print(f"    [{item['level']}] {item['connector_type']}: {item['description']}")

    # (e) UK inflation -> the curated ONS CPI catalog (dataset MM23).
    # Free text finds the whole family; country='GB' also returns the BoE
    # rate series and the OECD UK share-price proxy from (c2), so filter on
    # connector_type='ons' for CPI only.
    step("(e) Resolve 'UK inflation'")
    resp_e = api.connectors.search(q="UK inflation", limit=200)
    print(f"  Found {resp_e['pagination']['total']} results")
    headline = [i for i in resp_e["data"] if i["name"] in ("D7BT", "D7G7")]
    for item in headline:
        print(f"    [{item['level']}] {item['connector_type']}/{item['name']}: {item['description']}")
    # One COICOP division resolves to its index, annual rate, expenditure
    # weight and contribution -- everything needed to decompose the headline.
    resp_e7 = api.connectors.search(q="COICOP 07", limit=200)
    print(f"  Transport (COICOP 07): "
          f"{sorted(i['name'] for i in resp_e7['data'])}")
    # Fetch them: the CDIDs go straight into an `ons` connector config.
    print("  -> connector config: "
          "{'series': ['D7BT', 'D7G7', 'D7C2', 'CHZX'], 'dataset': 'MM23'}")

    # Bonus: free-text search
    step("Free-text search: 'treasury'")
    resp_q = api.connectors.search(q="treasury")
    print(f"  Found {resp_q['pagination']['total']} results matching 'treasury'")
    for item in resp_q["data"][:5]:
        tenor_str = f" (tenor={item['tenor']})" if item.get("tenor") else ""
        print(f"    {item['name']}: {item['description']}{tenor_str}")

    print("\nDone.")


if __name__ == "__main__":
    main()

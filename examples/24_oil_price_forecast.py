"""24 -- Oil-price forecast: EIA prices + CFTC positioning -> WTI forecast.

An energy-grade end-to-end run on live data:
    EIA connector (WTI + Brent spot prices) + CFTC connector (managed-money
    positioning) -> domain -> platform -> explainable time-series forecast
    of the WTI crude oil spot price.

Bring your own EIA key (free: https://www.eia.gov/opendata/register.php).
Add it to examples/.env as:
    EIA_API_KEY=your_eia_key

    python 24_oil_price_forecast.py
"""

import os
import sys

from _common import banner, get_client, step, wait_for_domain
from ambertraceai import AmbertraceError

# EIA series: WTI + Brent weekly spot prices + inventories
EIA_SERIES = ["PET.RWTC.W", "PET.RBRTE.W", "PET.WCESTUS1.W"]
# CFTC: WTI managed-money positioning (disaggregated report)
CFTC_CODES = ["067651"]
TARGET = "PET.RWTC.W"  # Forecast WTI crude oil


def _config_status(api, platform_id, config_id, *, timeout=300, poll_interval=5) -> str:
    import time
    deadline = time.monotonic() + timeout
    while True:
        cfg = next((c for c in api.predictions.list_configs(platform_id)
                    if c.get("id") == config_id), None)
        status = (cfg or {}).get("status", "")
        if status in ("trained", "failed", "error") or time.monotonic() >= deadline:
            return status
        time.sleep(poll_interval)


def main() -> None:
    eia_key = os.environ.get("EIA_API_KEY")
    if not eia_key:
        sys.exit(
            "Set EIA_API_KEY in examples/.env "
            "(free at https://www.eia.gov/opendata/register.php)."
        )

    api = get_client()
    banner("Oil-price forecast (EIA + CFTC)")

    domain = api.domains.create(
        name="SDK Example -- Oil Price",
        description=(
            "WTI/Brent crude oil spot prices, US inventories (EIA), "
            "and managed-money futures positioning (CFTC)."
        ),
    )
    domain_id = domain["id"]
    step(f"Created domain #{domain_id}")

    platform_id = None
    try:
        # Fetch EIA price + inventory data.
        dataset = api.datasets.fetch_multi(
            domain_id=domain_id,
            sources=[
                {
                    "connector_type": "eia",
                    "config": {
                        "api_key": eia_key,
                        "series_ids": EIA_SERIES,
                        "frequency": "weekly",
                    },
                },
                {
                    "connector_type": "cftc",
                    "config": {
                        "report": "disaggregated",
                        "commodity_codes": CFTC_CODES,
                    },
                },
            ],
            frequency="weekly",
        )
        step(f"Ingested EIA + CFTC data: dataset #{dataset.get('id')}")

        api.domains.build_ontology(domain_id)
        if wait_for_domain(api, domain_id, timeout=240).get("status") != "active":
            step("Ontology build did not complete; aborting.")
            return

        result = api.platforms.create(domain_id=domain_id, dataset_id=dataset["id"])
        platform_id = result["platform"]["id"]
        api.wait_for_job(result["build_job"]["id"], timeout=600, type='build')
        step(f"Platform #{platform_id} built")

        config = api.predictions.create_config(
            platform_id, mode="timeseries", target_field=TARGET,
            time_index_field="date", horizon=4, frequency="weekly",
        )
        api.predictions.train(platform_id, config["id"])
        status = _config_status(api, platform_id, config["id"])
        step(f"Training: {status}")

        if status == "trained":
            forecast = api.predictions.predict(
                platform_id, prediction_config_id=config["id"])
            step(
                f"4-week {TARGET} forecast: "
                f"{forecast.get('prediction') or forecast}"
            )
        api.predictions.delete_config(platform_id, config["id"])
    except AmbertraceError as e:
        print(f"\n  ! API error {e.status_code} ({e.code}): {e}")
    finally:
        if platform_id:
            api.platforms.delete(platform_id)
        api.domains.delete(domain_id)
        step(f"Cleaned up platform + domain #{domain_id}")

    print("\n  Oil-price forecast walkthrough complete.")


if __name__ == "__main__":
    main()

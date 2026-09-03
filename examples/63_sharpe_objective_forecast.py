"""63 -- Sharpe-ratio objective forecast.

Demonstrates the ``objective`` field on PredictionConfig (#2034): creating a
prediction config with ``objective='sharpe_ratio'`` so the acceptance gate
optimises for RISK-ADJUSTED directional PnL instead of the default
skill-vs-persistence metric.

The per-objective trading metrics (directional_pnl, hit_rate, sharpe_ratio,
max_drawdown) are surfaced in the symbolic-forecast response metadata when the
config declares a ``frequency``.

    python 63_sharpe_objective_forecast.py

.. note::

   The ``objective`` field is available from the SDK release shipping with
   #2034 increments 3-4.  The SDK-release train carries it.
"""

import argparse
import sys

from _common import api, ensure_domain_platform_data

EXAMPLE_DATASET = "data/fred_economic_data.csv"


def main():
    parser = argparse.ArgumentParser(
        description="Sharpe-ratio objective forecast example")
    parser.add_argument(
        "--dataset", default=EXAMPLE_DATASET,
        help="Path to the dataset CSV (default: %(default)s)")
    args = parser.parse_args()

    # --- Setup: domain + platform + data ---
    platform_id = ensure_domain_platform_data(
        domain_name="sharpe_objective_demo",
        dataset_path=args.dataset,
    )

    # --- Create prediction config with objective='sharpe_ratio' ---
    config_resp = api.create_prediction_config(
        id=platform_id,
        data={
            "target_field": "GS10",
            "time_index_field": "date",
            "frequency": "monthly",
            "objective": "sharpe_ratio",
        },
    )
    config = config_resp.data
    print(f"Created config id={config['id']} objective={config['objective']}")
    assert config["objective"] == "sharpe_ratio"

    # --- Train ---
    train_resp = api.train_prediction_model(
        id=platform_id,
        config_id=config["id"],
    )
    print(f"Training status: {train_resp.data.get('status', 'unknown')}")

    # --- Symbolic forecast (surfaces the per-objective metrics) ---
    forecast_resp = api.symbolic_forecast(
        id=platform_id,
        data={"config_id": config["id"]},
    )
    forecast = forecast_resp.data

    # The response surfaces backtest-fit skill + objective-specific metrics
    print(f"Skill vs persistence: {forecast.get('skill_vs_persistence')}")
    print(f"Objective: {forecast.get('objective')}")
    print(f"Objective value: {forecast.get('objective_value')}")

    # Trading metrics are in the response when frequency is set
    for key in ("directional_pnl", "hit_rate", "sharpe_ratio", "max_drawdown"):
        val = forecast.get(key)
        if val is not None:
            print(f"  {key}: {val}")

    print("Done.")


if __name__ == "__main__":
    sys.exit(main() or 0)

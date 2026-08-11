"""57 — UK 10Y breakeven inflation macro forecast (let the SYSTEM pick the drivers, in rules you can read).

Same premise as the other macro demos (bond, S&P, Bitcoin, inflation, credit, GDP): don't
hand-pick features. Give the platform a neutral panel of UK macro drivers and let it tell you
which ones explain the target — with the readable rules to back it.

The target is UK 10-year BREAKEVEN inflation: the market-priced inflation rate implied by the gap
between index-linked and conventional gilts (Bank of England fitted curve). Unlike 32 (US realised
CPI), this is the market's forward inflation EXPECTATION.

  1. Upload a bundled MONTHLY panel — target ``bei_10_0y``, drivers BoE Bank Rate + SONIA, ONS CPI
     %y/y, oil, GBP/USD, UK unemployment, UK business confidence (``data/bei_10y_panel.csv``).
  2. Build a verified platform and train a SPARSE-LINEAR forecaster (``model_type="lasso"``) with
     autoregression OFF and a first-difference target transform — so the model explains the
     breakeven CHANGE through the driver panel, not its own momentum.
  3. Read back what the SYSTEM selected: neural feature importance (which drivers it keeps), the
     induced WHEN->THEN driver rules (the WHY), and the neuro-symbolic discovery pass.

To fetch the panel LIVE instead of using the bundled snapshot, use ``fetch_multi`` with the
``tenors`` filter on the ``boe_yield_curves`` connector to keep only the 10Y breakeven::

    dataset = api.datasets.fetch_multi(
        domain_id=domain["id"],
        sources=[
            {"connector_type": "boe_yield_curves",
             "config": {"curve_types": ["inflation"], "tenors": [10.0]}},
            {"connector_type": "fred", "config": {"series_id": "..."}},
        ],
    )

Why lasso, not gbt: on this panel sparse linear beats boosted trees on the level fit (R² 0.75 vs
0.62) and is the only one that matches a last-value baseline on the genuinely hard month-to-month
change (change R² +0.02 vs -0.51). When the signal is a few slow macro drivers, the model forced to
be sparse finds them instead of fitting noise.

Honest framing: the value is an EXPLAINABLE fit — a strong read on the level, readable rules over
real macro drivers, and change-space skill right at the last-value baseline. Not a market-beating
monthly signal, and it doesn't claim to be.

LIVE RESULTS (bundled snapshot; confirm with a fresh run): level R²=0.75, change R²=+0.02 over 350
monthly rows (1997–2026); kept drivers led by oil (~0.88) with business confidence (~0.12). The
induced rules read as easing dynamics — falling short-rate momentum (Bank Rate / SONIA) pushes
breakevens up. Neuro-symbolic discovery accepts 0 correction rules: the driver panel already
explains the level.

DATA: BoE (UK Open Government Licence v3.0), ONS (Crown Copyright, OGL v3.0), FRED (US-government /
OECD public-domain). Bundled snapshot; no API key needed. Point-in-time; sources revise.

    python 57_uk_breakeven_inflation_forecast.py             # build on the bundled snapshot
    python 57_uk_breakeven_inflation_forecast.py --standard  # skip the verified profile
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from _common import (
    add_common_args,
    add_verified_args,
    build_ontology,
    build_platform,
    print_dataset,
    print_section,
    run_demo,
    train_prediction_model,
)

DATA_DIR = Path(__file__).resolve().parent / "data"
DEFAULT_DATASET = DATA_DIR / "bei_10y_panel.csv"
TARGET = "bei_10_0y"
# Sparse linear beats boosted trees on this panel — better level fit AND the only model that
# matches a last-value baseline on the month-to-month change (see the module docstring).
MODEL_TYPE = "lasso"

DOMAIN_NAME = "UK 10Y breakeven inflation (system feature selection)"
# Keep this a PLAIN column-name list. Pairing a column with a descriptive alias (e.g.
# "ons_cpi_yoy, headline CPI rate") makes the ontology builder emit entity properties that don't
# reconcile against the dataset's real columns, and the verified build fails with a schema error.
DOMAIN_DESCRIPTION = (
    "Forecast bei_10_0y from boe_bank_rate, boe_sonia, ons_cpi_yoy, oil, gbpusd, "
    "uk_unemployment, and uk_business_confidence."
)

# Split an engineered feature name back to its base series, e.g. oil_rollchg_3 -> oil.
_SUFFIX_RE = re.compile(r"_(rollmean|rollstd|rollchg|rolldev|pctchg|lag|roc|chg|diff|zscore)")


def _aggregate_importance(feature_importance: list) -> list[tuple[str, float]]:
    """Sum engineered-feature importance back to base series (drop _lag_/_roc_/... suffixes)."""
    base: dict[str, float] = defaultdict(float)
    for x in feature_importance or []:
        name = x.get("feature") if isinstance(x, dict) else x[0]
        imp = (x.get("importance") if isinstance(x, dict) else x[1]) or 0
        base[_SUFFIX_RE.split(name)[0]] += imp
    return sorted(base.items(), key=lambda kv: -kv[1])


def _print_fit(prediction: dict[str, Any]) -> None:
    """Print the backtest FIT — level, the honest month-to-month change, and skill context."""
    model = (prediction.get("explanation") or {}).get("model") or {}
    metrics = model.get("metrics") or {}
    level = metrics.get("level") or {}
    transformed = metrics.get("transformed") or {}
    r2 = level.get("r2", model.get("r2"))
    rmse = level.get("rmse", model.get("rmse"))
    skill = metrics.get("skill_vs_persistence", model.get("skill_vs_persistence"))
    print(f"  fit (level): R^2={r2}, RMSE={rmse}")
    if isinstance(transformed.get("r2"), (int, float)):
        print(f"  fit (month-to-month change): R^2={transformed.get('r2')} — the honest hard part; "
              "matching a last-value baseline (R^2~0) is the bar here.")
    if isinstance(skill, (int, float)):
        print(f"  (skill_vs_persistence={skill:+.3f} — +ve edges a last-value baseline.)")


def run_bei_forecast(api, args: argparse.Namespace) -> None:
    if not args.dataset.exists():
        print(f"ERROR: {args.dataset} not found.", file=sys.stderr)
        sys.exit(1)
    total = 5

    print_section(1, total, "Creating domain + uploading the bundled UK BEI 10Y driver panel")
    domain = api.domains.create(name=DOMAIN_NAME, description=DOMAIN_DESCRIPTION)
    dataset = api.datasets.upload(domain_id=domain["id"], file_path=str(args.dataset))
    print_dataset(dataset)

    print_section(2, total, "Building ontology + verified platform")
    build_ontology(api, domain["id"])
    platform = build_platform(
        api, domain["id"], dataset["id"],
        verified_profile=not args.standard, verified_min_confidence=args.tau)
    pid = platform["id"]
    # lasso: sparse linear (see docstring). autoregressive="none": explain the breakeven through
    # the driver panel, not its own momentum. difference transform: the level is ~a random walk.
    cfg = api.predictions.create_config(
        pid, mode="timeseries", target_field=TARGET, time_index_field="date",
        horizon=args.horizon, frequency="monthly", model_type=MODEL_TYPE,
        autoregressive=args.autoregressive,
        feature_config={"target_transform": "difference"})
    cfg = train_prediction_model(api, pid, cfg["id"])

    print_section(3, total, "What the SYSTEM selected — the sparse-linear fit")
    ar_note = ("drivers only — no target own-history features"
               if args.autoregressive == "none" else args.autoregressive)
    print(f"  model_type={MODEL_TYPE}  autoregressive={args.autoregressive} ({ar_note})")
    base = api.predictions.predict(pid, prediction_config_id=cfg["id"])
    _print_fit(base)
    ranking = _aggregate_importance((base.get("explanation") or {}).get("feature_importance"))
    kept = [(b, i) for b, i in ranking if i > 0 and b != "date"]
    print(f"  the model kept {len(kept)} driver series with non-zero importance "
          "(aggregated by base series):")
    for b, imp in kept:
        print(f"    {b:22s} {imp:.4f}")

    print_section(4, total, "The WHY — induced WHEN-THEN driver rules you can read")
    sf = api.predictions.symbolic_forecast(
        pid, prediction_config_id=cfg["id"], verified=not args.standard)
    why = sf.get("why") or []
    print(f"  {len(why)} driver rules induced — each carries a contribution, a confidence band "
          "and a historical hit-rate (the model's readable explanation, not a rival forecaster).")
    for w in sorted(why, key=lambda x: -abs(x.get("contribution") or 0)):
        d = str(w.get("driver"))[:80]
        print(f"    {w.get('direction')} {w.get('contribution'):+.4f} | {d}")

    print_section(5, total, "NEURO-SYMBOLIC — does a correction layer beat the model?")
    summary = api.predictions.discover_prediction_rules(
        pid, prediction_config_id=cfg["id"], timeout=args.discover_timeout)
    accepted = summary.get("total_accepted") or 0
    print(f"  rounds={summary.get('rounds')}  accepted={accepted} "
          f"rejected={summary.get('total_rejected')}")
    if accepted:
        print(f"  The symbolic correction layer added value: {accepted} discovered rule(s) beat "
              "the model backtest, held pending expert approval.")
    else:
        print("  No discovered correction rule beat the model — the driver panel already explains "
              "the breakeven level, and the layer honestly adds nothing here.")

    print(f"\nDone. Platform {pid}. The system chose the drivers and showed its working — an "
          "explainable fit + readable rules, not a market-beating signal.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="UK 10Y breakeven inflation macro forecast — let the system pick the drivers")
    add_common_args(parser)
    add_verified_args(parser)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET,
                        help="bundled BEI driver panel CSV")
    parser.add_argument("--horizon", type=int, default=1, help="forecast horizon in months")
    parser.add_argument("--autoregressive", choices=["full", "limited", "none"], default="none",
                        help="how much the model may use the target's own history (default: none)")
    parser.add_argument("--discover-timeout", type=float, default=1500.0,
                        help="seconds to wait for neuro-symbolic rule discovery")
    args = parser.parse_args()
    run_demo(run_bei_forecast, args)


if __name__ == "__main__":
    main()

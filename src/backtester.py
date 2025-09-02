"""
Aleph Sigma — minimal backtester skeleton (sanitized)
Demonstrates: no-lookahead logic, SL/TP handling, costs, single-position rules.
"""

from dataclasses import dataclass
import pandas as pd

@dataclass
class Costs:
    fee_per_lot: float = 4.5
    spread_price: float = 0.07
    contract_size: int = 100

@dataclass
class RiskConfig:
    risk_pct: float = 0.01     # 1%
    sl_pips: float = 70.0
    rr: float = 7.0            # do not disclose your tuned values if you prefer
    pip_size: float = 0.01
    max_lot_size: float = 100.0

class AlephSigmaBacktester:
    def __init__(self, minute_df: pd.DataFrame, second_df: pd.DataFrame,
                 costs: Costs, risk: RiskConfig):
        self.minute = minute_df.copy()
        self.second = second_df.copy()
        self.costs = costs
        self.risk = risk
        # ensure chronological order
        for df in (self.minute, self.second):
            if not df.empty:
                df.sort_values("datetime", inplace=True)

    def run(self) -> dict:
        """Run a conservative, one-position backtest with SL-before-TP rule."""
        # NOTE: This is a template; real logic omitted intentionally.
        return {
            "total_trades": 0,
            "win_rate": 0.0,
            "profit_factor": 0.0,
            "max_drawdown": 0.0,
        }

if __name__ == "__main__":
    # Example entry point — use dummy/sample data only.
    print("Aleph Sigma template ready. See docs/ for the research note.")


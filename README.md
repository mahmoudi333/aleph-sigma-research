#  Aleph Sigma — Systematic Backtesting Research (XAUUSD)

_A fully systematic, rule-based strategy with conservative backtesting design_

---

##  Overview
This repository showcases **Aleph Sigma**, a fully systematic volatility-spike strategy and a conservative backtesting framework.

- **Systematic, non-discretionary**: signal → arm stop-order at signal price → if touched, trade opens; only one position at a time.  
- **Risk model**: fixed **1% per trade** with **SL = 70 pips**, **RR = 7**.  
- **Transaction costs**: $4.5 per lot fee and 0.07 spread included.  
- **No look-ahead**: indicators use past info only; exits checked per second, **SL-before-TP** to avoid false wins.  

> **Important:** This repo contains a **sanitized code skeleton** for structure and review. Exact tuned parameters and proprietary datasets are not included.

---

##  Key Results (2020–2025)
- Profit Factor: **1.2 – 1.4**  
- Sharpe Ratio: **1.0 – 1.8**  
- Max Drawdown: **19% – 47%**  
- Annual ROI: **182% – 479%**  
- Consistently **net positive each year**  

📄 Full research note: [`docs/Aleph_Sigma_Strategy_Research_Note.pdf`](docs/Aleph_Sigma_Strategy_Research_Note.pdf)  
📊 Trade log (2024–2025): [`docs/aleph_sigma_backtest.xlsx`](docs/aleph_sigma_backtest.xlsx)  
## ✅ How to Validate a Trade
Use `docs/aleph_sigma_backtest.xlsx` (2024–2025):
1) Head over to https://www.dukascopy.com/swiss/english/marketwatch/charts/
2) Select XAUUSD and set the chart to a 1-second timeframe.
3) Open docs/aleph_sigma_backtest.xlsx and pick any trade (win or loss).
4) Hover over dukascopy chart and press Alt+H three time to draw horizon price lines entry sl and tp
5) Double-click each line and set the prices to the Entry, Stop-Loss, and Take-Profit from the spreadsheet.
6) Confirm the **entry second** by using "show custom time range" feature on dukascopy (magnifying glass icon) and matching the entry_time there.

---

## 🔁 Order Lifecycle & Signal Replacement Policy

This strategy maintains **at most one pending order** and **at most one active position** at any time.

### Key invariants
- **One position max**: never open more than one trade at a time.  
- **One pending order max**: never stack multiple unfilled signals.  
- **No same-bar fills**: a signal armed at bar *j* can only trigger on a later bar (*k > j*).  

### Lifecycle
1. **Signal detected → Arm order**  
   - Signal at minute *j* creates a pending stop order with entry, SL, and TP.  

2. **Trigger check on subsequent minutes (k > j)**  
   - If touched, order triggers, becomes **Active**, and entry is time-stamped using **sorted second-level data** inside that minute.  

3. **Exit logic (per second, conservative)**  
   - From entry second onward, check **SL before TP**.  
   - If both hit in the same second → **Loss** (worst-case tie-break).  
   - When SL or TP is reached, position closes.  

4. **Replacement of unfilled signals**  
   - If a new signal appears before the armed order is triggered, it **replaces** the old one.  
   - Earlier unfilled order is discarded.  

### Why replace instead of queue?
- Keeps risk simple and transparent.  
- Avoids ambiguity in bar data (no order book simulation).  
- Focuses exposure on the **freshest signal regime**.  

```mermaid
stateDiagram-v2
    [*] --> IDLE
    IDLE --> ARMED: signal@j → arm stop
    ARMED --> ACTIVE: k>j & price touches entry
    ACTIVE --> IDLE: SL/TP exit (per-second, SL before TP)
    ARMED --> ARMED: new signal replaces pending

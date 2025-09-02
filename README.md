# Aleph Sigma — Systematic Backtesting Research (XAUUSD)

This repository showcases **Aleph Sigma**, a fully systematic, rule-based strategy and a conservative backtesting framework.

- **Systematic, non-discretionary**: signal → arm stop-order at signal price → if touched, trade opens; only one position at a time.
- **Risk model**: fixed **1% per trade** with **SL = 70 pips**, **RR = 7**.
- **Transaction costs**: **$4.5 per lot** fee and **0.07** spread included.
- **No look-ahead**: indicators use past info only; SL is checked before TP on each second to avoid false wins.

> **Important:** This repo contains a **sanitized code skeleton** for structure and review. Exact, tuned parameters and proprietary datasets are not included.

## What’s here
- `docs/Aleph_Sigma_Strategy_Research_Note.pdf` – 2–3 page research note (results & methodology)
- `src/backtester.py` – minimal, sanitized backtester structure
- `requirements.txt` – Python dependencies

## Contact
- Email: mahmoudioussama@icloud.com
- GitHub: https://github.com/mahmoudi333

*License: MIT*

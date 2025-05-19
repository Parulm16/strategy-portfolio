# 📊 Strategy Portfolio for Python Trading Developer Role

Welcome! This repository showcases algorithmic trading strategies built using Python and financial market data. The goal is to demonstrate technical skills in:

- Data analysis
- Trading logic implementation
- Backtesting
- Visualization
- Clean code and modular design

---

## 📁 Structure

├── oi_volume_strategy/
│ ├── sample_data.csv # Sample OI + price + volume data
│ ├── oi_volume_signal.py # Signal generation logic
│ ├── oi_volume_backtest.py # Backtesting logic
│
├── run_strategy.py # Executes signal generation
├── run_backtest.py # Runs backtest and prints results
├── plot_performance.py # Plots cumulative returns
├── README.md # Project overview
└── requirements.txt # Python packages

This strategy interprets trader behavior by analyzing:

- 🔼 Price Change
- 🔼 Open Interest (OI) Change
- 🔼 Volume Change *(optional extension)*

### Signal Logic:

| Price Change | OI Change | Interpretation     |
|--------------|-----------|--------------------|
| ↑            | ↑         | **Long Buildup**   |
| ↓            | ↑         | **Short Buildup**  |
| ↑            | ↓         | **Short Covering** |
| ↓            | ↓         | **Long Unwinding** |

### Features:
- Classifies daily market behavior using price and OI data.
- Simple rule-based backtesting engine.
- Visualizes cumulative returns over time.

---

## 📈 Example Output

```bash
        Date     Close     Signal           Position  Returns  Cumulative_Returns
0  2024-01-01    19500     No Clear Signal     0       0.000         0.000
1  2024-01-02    19600     Long Buildup        1       0.000         0.000
2  2024-01-03    19400     Short Buildup       0       0.010         0.010
3  2024-01-04    19550     Short Covering      1       0.000         0.010
4  2024-01-05    19480     Long Unwinding      0       0.003         0.013

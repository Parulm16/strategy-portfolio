# Pair Trading
This strategy identifies trading opportunities between two co-moving indices (e.g., NIFTY and BANKNIFTY). It uses linear regression to estimate a hedge ratio and trades the spread when it diverges significantly from the mean (based on Z-score).

**Signal Logic:**
- Z > 1 → Short Spread
- Z < -1 → Long Spread
- Z ≈ 0 → Exit
  
- `pair_signal.py`: Calculates hedge ratio, spread, and Z-score-based signals
- `pair_backtest.py`: Computes returns from the strategy
- `pair_plot.py`: Visualizes the performance
- `pair_data.csv`: Sample 2025 data (Jan–Mar)

To run:

```bash
python plot_pair_performance.py

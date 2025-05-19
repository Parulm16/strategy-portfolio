import pandas as pd
from oi_volume_signal import classify_oi_price_behavior
from oi_volume_backtest import backtest_oi_strategy

# Load data
df = pd.read_csv(r"C:\Users\Admin\Desktop\Strategy-portfolio\oi_volume_strategy\sample_data.csv", parse_dates=['Date'])

# Generate signals
df = classify_oi_price_behavior(df)

# Run backtest
df = backtest_oi_strategy(df)

# Show results
print(df[['Date', 'Close', 'Signal', 'Position', 'Returns', 'Cumulative_Returns']])

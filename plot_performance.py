import pandas as pd
import matplotlib.pyplot as plt
from oi_volume_signal import classify_oi_price_behavior
from oi_volume_backtest import backtest_oi_strategy

# Load data
df = pd.read_csv(r"C:\Users\Admin\Desktop\Strategy-portfolio\oi_volume_strategy\sample_data.csv", parse_dates=['Date'])

# Generate signals
df = classify_oi_price_behavior(df)

# Run backtest
df = backtest_oi_strategy(df)

# Plot cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Cumulative_Returns'], label='Strategy Cumulative Returns', color='blue')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.title('OI + Volume Strategy Performance')
plt.legend()
plt.grid(True)
plt.show()

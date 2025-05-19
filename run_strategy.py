import pandas as pd
from oi_volume_signal import classify_oi_price_behavior

# Load the sample data
df = pd.read_csv(r"C:\Users\Admin\Desktop\Strategy-portfolio\oi_volume_strategy\sample_data.csv", parse_dates=['Date'])

# Run the signal classifier
df = classify_oi_price_behavior(df)

# Print the last few rows to see signals
print(df[['Date', 'Close', 'Open_Interest', 'Signal']])

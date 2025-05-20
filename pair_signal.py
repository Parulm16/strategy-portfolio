# pair_signal.py
import pandas as pd
import statsmodels.api as sm

def generate_signals(data_path):
    df = pd.read_csv(data_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Linear regression to get hedge ratio (beta)
    X = sm.add_constant(df['BANKNIFTY'])
    y = df['NIFTY']
    model = sm.OLS(y, X).fit()
    beta = model.params['BANKNIFTY']

    # Spread and Z-Score
    df['Spread'] = df['NIFTY'] - beta * df['BANKNIFTY']
    df['Spread_Mean'] = df['Spread'].rolling(window=20).mean()
    df['Spread_Std'] = df['Spread'].rolling(window=20).std()
    df['Z-Score'] = (df['Spread'] - df['Spread_Mean']) / df['Spread_Std']

    # Signal logic
    def signal_logic(z):
        if z > 1:
            return -1  # Short spread
        elif z < -1:
            return 1   # Long spread
        elif abs(z) < 0.2:
            return 0   # Exit
        else:
            return None

    df['Signal'] = df['Z-Score'].apply(signal_logic).ffill()
    return df

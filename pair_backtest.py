# pair_backtest.py
import pandas as pd
from pair_signal import generate_signals

def backtest_strategy(data_path):
    df = generate_signals(data_path)

    df['Return_A'] = df['NIFTY'].pct_change()
    df['Return_B'] = df['BANKNIFTY'].pct_change()

    # Beta was calculated in signal generation
    beta = (df['NIFTY'] - df['Spread']) / df['BANKNIFTY']
    df['Beta'] = beta

    df['Strategy_Return'] = df['Signal'].shift(1) * (df['Return_A'] - df['Beta'] * df['Return_B'])
    df['Cumulative_Return'] = (1 + df['Strategy_Return'].fillna(0)).cumprod()

    return df

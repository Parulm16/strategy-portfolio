import pandas as pd

def backtest_oi_strategy(df):
    """
    A simple backtest:
    - Buy when signal is 'Long Buildup'
    - Sell/short when signal is 'Short Buildup'
    - Exit positions on opposite signals or 'No Clear Signal'
    """
    df = df.copy()

    # Initialize columns
    df['Position'] = 0  # 1 for long, -1 for short, 0 for flat
    df['Returns'] = 0.0

    position = 0  # current position
    entry_price = 0

    for i in range(1, len(df)):
        signal = df.loc[i, 'Signal']
        price = df.loc[i, 'Close']

        # Enter long position
        if signal == 'Long Buildup' and position == 0:
            position = 1
            entry_price = price
            df.at[i, 'Position'] = position

        # Enter short position
        elif signal == 'Short Buildup' and position == 0:
            position = -1
            entry_price = price
            df.at[i, 'Position'] = position

        # Exit long if short buildup signal or no clear signal
        elif position == 1 and signal in ['Short Buildup', 'No Clear Signal']:
            df.at[i, 'Returns'] = (price - entry_price) / entry_price
            position = 0
            df.at[i, 'Position'] = position

        # Exit short if long buildup signal or no clear signal
        elif position == -1 and signal in ['Long Buildup', 'No Clear Signal']:
            df.at[i, 'Returns'] = (entry_price - price) / entry_price
            position = 0
            df.at[i, 'Position'] = position

        else:
            df.at[i, 'Position'] = position

    # Calculate cumulative returns
    df['Cumulative_Returns'] = (1 + df['Returns']).cumprod() - 1

    return df

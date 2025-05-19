import pandas as pd

def classify_oi_price_behavior(df):
    """
    Classify behavior based on price and open interest change.
    """
    df = df.copy()
    
    # Calculate % change in Close price and Open Interest
    df['Price_Change'] = df['Close'].pct_change()
    df['OI_Change'] = df['Open_Interest'].pct_change()

    def classify(row):
        if row['Price_Change'] > 0 and row['OI_Change'] > 0:
            return 'Long Buildup'
        elif row['Price_Change'] < 0 and row['OI_Change'] > 0:
            return 'Short Buildup'
        elif row['Price_Change'] > 0 and row['OI_Change'] < 0:
            return 'Short Covering'
        elif row['Price_Change'] < 0 and row['OI_Change'] < 0:
            return 'Long Unwinding'
        else:
            return 'No Clear Signal'

    # Apply classification
    df['Signal'] = df.apply(classify, axis=1)
    return df

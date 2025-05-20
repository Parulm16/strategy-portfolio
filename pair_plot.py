# pair_plot.py
import matplotlib.pyplot as plt
from pair_backtest import backtest_strategy

def plot_results(data_path):
    df = backtest_strategy(data_path)

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Cumulative_Return'], label='Pair Trading Strategy')
    plt.title('Cumulative Returns of Pair Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

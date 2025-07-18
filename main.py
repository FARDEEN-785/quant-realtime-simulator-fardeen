import ccxt
import pandas as pd
import time
import matplotlib.pyplot as plt
from config import SYMBOL, TIMEFRAME, LIMIT
from strategy import generate_macd_signals
from wallet import execute_trade

# Create exchange instance
exchange = ccxt.bybit()

def fetch_data():
    market = SYMBOL.replace("/", "")
    bars = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit=LIMIT)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def plot_chart(df, actions):
    plt.figure(figsize=(12, 8))
    
    # Price chart
    plt.subplot(2, 1, 1)
    plt.plot(df['timestamp'], df['close'], label='Close Price', color='blue')
    buy_signals = [i for i, a in enumerate(actions) if a == 'buy']
    sell_signals = [i for i, a in enumerate(actions) if a == 'sell']
    plt.scatter(df['timestamp'].iloc[buy_signals], df['close'].iloc[buy_signals], marker='^', color='green', label='Buy Signal', zorder=5)
    plt.scatter(df['timestamp'].iloc[sell_signals], df['close'].iloc[sell_signals], marker='v', color='red', label='Sell Signal', zorder=5)
    plt.title("Price & Buy/Sell Signals")
    plt.legend()

    # MACD chart
    plt.subplot(2, 1, 2)
    plt.plot(df['timestamp'], df['macd'], label='MACD', color='purple')
    plt.plot(df['timestamp'], df['signal'], label='Signal Line', color='orange')
    plt.axhline(0, color='gray', linestyle='--')
    plt.title("MACD Indicator")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = fetch_data()
    actions = []

    # Run strategy
    signal = generate_macd_signals(df)
    actions = ['hold'] * (len(df) - 1) + [signal]

    # Execute trade on last candle
    last_price = df['close'].iloc[-1]
    print(f"Signal: {signal} | Price: {last_price}")
    execute_trade(signal, last_price)

    # Plot everything
    plot_chart(df, actions)

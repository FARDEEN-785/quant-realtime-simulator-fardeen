import pandas as pd   
from config import MACD_FAST , MACD_SLOW , SIGNAL


def generate_macd_signals(df):
    df['ema_fast'] = df['close'].ewm(span=MACD_FAST, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=MACD_SLOW, adjust=False).mean()
    df['macd'] = df['ema_fast'] - df['ema_slow']
    df['signal'] = df['macd'].ewm(span=SIGNAL , adjust=False).mean()
    
    
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    
    if prev['macd'] < prev['signal'] and last['macd'] > last['signal']:
        return 'buy'
    elif prev['macd'] > prev['signal'] and last['macd'] < last['signal']:
        return 'sell'
    else:
        return 'hold'
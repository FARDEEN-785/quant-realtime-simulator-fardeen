from config import START_BALANCE
import csv
from datetime import datetime

wallet = {
    'balance': START_BALANCE,
    'position': None,
    'entry_price': None
}

def execute_trade(action, price):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    if action == 'buy' and wallet['position'] is None:
        wallet['position'] = 'long'
        wallet['entry_price'] = price
        log_trade('BUY', price, wallet['balance'], timestamp)

    elif action == 'sell' and wallet['position'] == 'long':
        profit = price - wallet['entry_price']
        wallet['balance'] += profit
        wallet['position'] = None
        wallet['entry_price'] = None
        log_trade('SELL', price, wallet['balance'], timestamp)

def log_trade(action, price, balance, timestamp):
    with open('trade_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, action, price, balance])

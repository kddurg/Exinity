import random
import time

def simulate_streaming_data():
    symbols = ['AAPL', 'GOOGL', 'TSLA']
    while True:
        symbol = random.choice(symbols)
        open_price = random.uniform(100, 500). # taken this values for examples
        high_price = open_price + random.uniform(0, 10)
        low_price = open_price - random.uniform(0, 10)
        close_price = random.uniform(low_price, high_price)
        volume = random.randint(1, 1000)

        # Insert the streaming bar into the database
        insert_ohlc(symbol, open_price, high_price, low_price, close_price, volume)
        
        print(f"Inserted: {symbol}, Open: {open_price}, High: {high_price}, Low: {low_price}, Close: {close_price}, Volume: {volume}")
        time.sleep(1)  # Sleep for 1 second before generating the next bar
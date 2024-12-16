def insert_ohlc(symbol, open_price, high_price, low_price, close_price, volume):
    cursor.execute('''
    INSERT INTO ohlc (symbol, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)
    ''', (symbol, open_price, high_price, low_price, close_price, volume))
    conn.commit()
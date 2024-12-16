import sqlite3

# Create or connect to the database
conn = sqlite3.connect('streaming_bars.db')
cursor = conn.cursor()

# Create table to store OHLC data
cursor.execute('''
CREATE TABLE IF NOT EXISTS ohlc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()



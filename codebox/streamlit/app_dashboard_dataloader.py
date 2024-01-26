import cryptowatch as cw
import numpy as np
import json
import sqlite3
import datetime

# Set your API Key

cw.api_key = "9bwwvg3Mr0HTnDyjsOeWOP0Xcm5bNvedlwCjPUNQx3Z81DqHYEbz4wV5"

# Assets
exchange_dict = {'BITFINEX': (['xrd', 'smr'], 'USD'),
                 'BINANCE': (['btc', 'eth'], 'USDT')}

# Fetch data for each asset from the respective exchanges
for key, value in exchange_dict.items():
    exchange = key
    assets = [asset.upper() for asset in value[0]]
    curr = value[1]

    for asset in assets:
        try:
            # Parse JSON
            parsed_data = json.loads(cw.markets.get(f"{exchange}:{asset}{curr}")._http_response.content)

            # Extract price and volume data
            result = parsed_data['result']
            price = result['price']
            volume = result['volume']
            volume_quote = result['volumeQuote']
            pct_change = price['change']['percentage']
            abs_change = price['change']['absolute']

            # Store the data
            data = (datetime.date.today(), asset, price['last'], price['high'],
                    price['low'], pct_change, abs_change, volume, volume_quote)

        except:
            print(f'No data for {asset}')
            # Store the data
            data = (datetime.date.today(), asset, np.nan, np.nan,
                    np.nan, np.nan, np.nan, np.nan, np.nan)

# Connect to the database
conn = sqlite3.connect('crypto_data.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS crypto_data 
             (date DATE, asset TEXT, last_price REAL, high_price REAL, 
             low_price REAL, pct_change REAL, abs_change REAL, volume REAL, volume_quote REAL)''')

for key, value in exchange_dict.items():
    exchange = key
    assets = [asset.upper() for asset in value[0]]
    curr = value[1]

    for asset in assets:
        try:
            # Parse JSON
            parsed_data = json.loads(cw.markets.get(f"{exchange}:{asset}{curr}")._http_response.content)

            # Extract price and volume data
            result = parsed_data['result']
            price = result['price']
            volume = result['volume']
            volume_quote = result['volumeQuote']
            pct_change = price['change']['percentage']
            abs_change = price['change']['absolute']

            # Prepare the data for insertion into the database
            data = (datetime.date.today(), asset, price['last'], price['high'],
                    price['low'], pct_change, abs_change, volume, volume_quote)

            # Insert the data into the table
            c.execute("INSERT INTO crypto_data VALUES (?,?,?,?,?,?,?,?,?)", data)
            conn.commit()

        except:
            print(f'No data for {asset}')
            # Prepare the data for insertion into the database
            data = (datetime.date.today(), asset, np.nan, np.nan,
                    np.nan, np.nan, np.nan, np.nan, np.nan)

            # Insert the data into the table
            c.execute("INSERT INTO crypto_data VALUES (?,?,?,?,?,?,?,?,?)", data)
            conn.commit()

# Close the connection
conn.close()
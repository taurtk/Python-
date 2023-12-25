import csv

# List of stock symbols for 10 Indian companies
stock_symbols = [
    'RELIANCE.NS',
    'TCS.NS',
    'HDFCBANK.NS',
    'HINDUNILVR.NS',
    'INFY.NS',
    'ICICIBANK.NS',
    'KOTAKBANK.NS',
    'ITC.NS',
    'BAJFINANCE.NS',
    'ONGC.NS',
]

# Specify the file name
csv_file = 'indian_stock_list.csv'

# Write the stock symbols to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Symbol'])  # Write the header
    writer.writerows(map(lambda x: [x], stock_symbols))

print(f"The CSV file '{csv_file}' has been created with Indian stock symbols.")

import requests
from bs4 import BeautifulSoup
import time

url = 'https://tradingeconomics.com/commodity/coal'  # Replace with the actual URL

def scrape_crude_oil_price():
    try:
        headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                  }

        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table element
        table = soup.find('table', class_='table-heatmap')
        # print(table)
        # Check if the table is found
        if table:
            # Find all rows in the table body
            print(type(table))
            rows = table.find_all('tr')
            # print(rows)
            # Iterate through rows and find the one with Crude Oil
            crude_oil_row = None
            for i in range(1,len(rows)):
                # print(rows[i])
                print(" ----------------------  ")
                commodity_name = rows[i].find('a').text.strip()
                if 'Crude Oil' in commodity_name:
                    crude_oil_row = rows[i]
                    break

            if crude_oil_row:
                # Extract price from the Crude Oil row
                crude_oil_price = crude_oil_row.find('td', id='p').text.strip()

                print(f"Crude Oil Price: {crude_oil_price}")
            else:
                print("Crude Oil row not found in the table.")
        else:
            print("Table not found in the HTML.")

    except Exception as e:
        print(f'Error: {e}')
        return None

while True:
    scrape_crude_oil_price()

    # Fetch data every 5 minutes
    time.sleep(300)

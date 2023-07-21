import requests
import pandas as pd
import json

# Replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=BRK-A&apikey=QEBX3VOR3USTQBNG&datatype=json'
response = requests.get(url)
data = response.json()

# Extracting the relevant financial data from the JSON response
df = pd.DataFrame(data['annualReports'])
selected_columns = ['fiscalDateEnding','totalAssets','totalCurrentAssets','totalNonCurrentAssets','shortTermDebt','longTermDebt','totalLiabilities','totalShareholderEquity']
filtered_df = df[selected_columns]
# pd.set_option("display.max_columns",100)
# pd.set_option("display.max_rows",4)
# filtered_df.to_excel("/workspaces/1205/BalanceSheet(filtered).xlsx", index=False)
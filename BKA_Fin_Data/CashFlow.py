import requests
import pandas as pd
import json

# Replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=BRK-A&apikey=QEBX3VOR3USTQBNG&datatype=json'
response = requests.get(url)
data = response.json()

# Extracting the relevant financial data from the JSON response
df = pd.DataFrame(data['annualReports'])
# selected_columns = ['fiscalDateEnding','operatingCashflow','cashflowFromInvestment','profitLoss']
# filtered_df = df[selected_columns]
# pd.set_option("display.max_columns",35)
# pd.set_option("display.max_rows",7)
print(df)

df.to_excel("/workspaces/1205/CashFlow(unfiltered).xlsx", index=False)
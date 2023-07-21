import requests
import pandas as pd
import json

# Replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=BRK-A&apikey=QEBX3VOR3USTQBNG&datatype=json'
response = requests.get(url)
data = response.json()

# Extracting the relevant financial data from the JSON response
df = pd.DataFrame(data['annualReports'])
# selected_columns = ['fiscalDateEnding','grossProfit','totalRevenue','netIncome']
# filtered_df = df[selected_columns]
print(df)

df.to_excel("/workspaces/1205/IncomeStatement(Unfiltered).xlsx", index=False)
import pandas as pd
import yfinance as yf
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows 

# Set the start and end dates
start_date = '2015-01-01'
end_date = '2015-12-31'

# Fetching data using yfinance
stock = yf.Ticker('BRK-A')
data = stock.history(start=start_date, end=end_date)

# Extracting financial attributes
revenue = data['Close'] * data['Volume']
net_income = revenue * 0.1
shares_outstanding = stock.info['sharesOutstanding']
eps = net_income / shares_outstanding
dividend_yield = data['Dividends'] / data['Close']
pe_ratio = data['Close'] / eps

# Print the extracted financial data
financial_data = pd.DataFrame({
    'Revenue': revenue,
    'Net Income': net_income,
    'EPS': eps,
    'Dividend Yield (%)': dividend_yield,
    'P/E Ratio': pe_ratio,
})

print(financial_data)
# wb = Workbook()
# ws = wb.create_sheet('Financial Data')

# for r in dataframe_to_rows(financial_data, header=True, index=False):
#     ws.append(r)
# wb.remove(wb['Sheet'])

# wb.save('/workspaces/1205/Financial_Data.xlsx')

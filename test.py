import yfinance as yf 
import pandas as pd 

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)

stock = yf.Ticker("BRK-A")

stock_info = stock.info
net_income = stock_info['Va(m)']
revenue = stock_info['totalRevenue']

print("Net Income:", net_income)
print("Revenue:", revenue)

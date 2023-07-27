import pandas as pd
import matplotlib.pyplot as plt

# Convert the data to a DataFrame
file_path = r'C:\Users\pauls\Downloads'
df = pd.read_excel(file_path)
#df = pd.read_excel(file_path, sheet_name='performance')

# Plotting revenue and net income
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Revenue'], label='Revenue', marker='o')
plt.plot(df['Date'], df['Net Income'], label='Net Income', marker='o')
plt.xlabel('Date')
plt.ylabel('Amount (in millions)')
plt.title('Revenue and Net Income Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting EPS
plt.figure(figsize=(8, 5))
plt.bar(df['Date'], df['EPS'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('EPS (in dollars)')
plt.title('Earnings Per Share Over Time')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Other visualizations can be created similarly for other columns



        

''' requests -> making HTTP requests
    BeautifulSoup -> parsing HTML
    tabulate -> formatting the data into a table'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows 

#sets the URL of the Wikipedia page to be scraped
url = "https://en.wikipedia.org/wiki/List_of_assets_owned_by_Berkshire_Hathaway"

# Send a GET request to the website & retrieve HTML content
response = requests.get(url)

# creates a BeautifulSoup object by parsing the HTML content 
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the fully owned companies
table = soup.find('table',{'class':'wikitable'})

# Create empty lists to store the data
company_data = []

# Iterate over the rows in the table
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) >= 3:
        company_name = columns[0].text.strip()
        company_description = columns[1].text.strip()
        company_stake = columns[2].text.strip().rstrip('%')
        company_stake = ''.join(filter(str.isdigit, company_stake))  # Extract only numeric characters
        if company_stake:  # Check if the value is not empty
            company_stake = int(company_stake)  # Convert stake to int
        else:
            company_stake = None  # Handle empty value

        company_data.append({
            "Company Name":company_name,
            "Description":company_description,
            "Stake":company_stake
        })

df = pd.DataFrame(company_data)
#filter companies fully owned by Berkshire Hathaway
filtered_df = df[df['Stake'] == 100]

#Storing the data in an excel sheet
wb = Workbook()
ws = wb.create_sheet('Company Owned')

for r in dataframe_to_rows(filtered_df, header=True, index=False):
    ws.append(r)
wb.remove(wb['Sheet'])
wb.save('/workspaces/1205/Company_owned(100).xlsx')
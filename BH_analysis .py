''' requests -> making HTTP requests
    BeautifulSoup -> parsing HTML
    tabulate -> formatting the data into a table'''
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#sets the URL of the Wikipedia page to be scraped
url = "https://en.wikipedia.org/wiki/List_of_assets_owned_by_Berkshire_Hathaway"

# Send a GET request to the website & retrieve HTML content
response = requests.get(url)

# creates a BeautifulSoup object by parsing the HTML content 
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the fully owned companies
table = soup.find('table',{'class':'wikitable'})

# Create empty lists to store the data
company_names = []
descriptions = []
Stake = []

# Iterate over the rows in the table
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) >= 3:
        company_name = columns[0].text.strip()
        company_description = columns[1].text.strip()
        company_stake = columns[2].text.strip()
        company_names.append(company_name)
        descriptions.append(company_description)
        Stake.append(company_stake)

# Create a list of lists containing the data
data = list(zip(company_names, descriptions, Stake))

# Display the data in a table format
headers = ["Company Name", "Description", "Stake"]
table = tabulate(data, headers, tablefmt="pipe")

# Print the table
print(table)
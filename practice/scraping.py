import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the website
url = "https://boodmo.com/vehicles/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Use the soup object to extract the relevant data, such as product names, descriptions, pricing, and image links.

# Step 3: Store the data in a CSV file
data = {'Product Name': product_names, 'Description': descriptions, 'Price': prices, 'Image Link': image_links}
df = pd.DataFrame(data)
df.to_csv('boodmo_data.csv', index=False)
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the website
url = "https://boodmo.com/vehicles/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Use the soup object to extract the relevant data, such as product names, descriptions, pricing, and image links.

# Step 3: Store the data in a CSV file
data = {'Product Name': product_names, 'Description': descriptions, 'Price': prices, 'Image Link': image_links}
df = pd.DataFrame(data)
df.to_csv('boodmo_data.csv', index=False)

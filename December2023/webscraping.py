import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Scrape the index page
index_url = "https://www.atoz-catering.co.uk/products"
response = requests.get(index_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the URLs of the individual pages
product_urls = [a['href'] for a in soup.find_all('a', href=True) if 'product' in a['href']]

# Step 2: Scrape the individual pages
product_info = []
for url in product_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract product name and price (replace 'product-name' and 'product-price' with actual classes)
    name = soup.find(class_='n-detail-product-name')
    price = soup.find(class_='mb-2 n-detail-price')
    
    if name and price:
        product_info.append({
            'Product Name': name.text,
            'Product Price': price.text
        })

# Save as a DataFrame
df = pd.DataFrame(product_info)

# Write to an Excel file
df.to_excel('products.xlsx', index=False)
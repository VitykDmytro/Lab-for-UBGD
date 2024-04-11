import requests
import pandas as pd

def get_available_products():
    url = "https://api.coinbase.com/v2/products"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print("Failed to retrieve available products.")
        return None

products = get_available_products()

if products:
    selected_products = products[:3]
    print("Selected products:", selected_products)

else:
    print("No products available.")

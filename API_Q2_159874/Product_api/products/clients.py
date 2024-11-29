import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/products/"

def add_product(name, description, price):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(BASE_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print("Product created successfully!")
        print(response.json())
    else:
        print(f"Failed to create product. Status code: {response.status_code}")
        print(response.json())

def get_products():
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        products = response.json()
        print("List of all products:")
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print(f"Failed to retrieve products. Status code: {response.status_code}")

def delete_product(product_id):
    url = f"{BASE_URL}{product_id}/"
    response = requests.delete(url)
    
    if response.status_code == 204:
        print("Product deleted successfully!")
    else:
        print(f"Failed to delete product. Status code: {response.status_code}")

if __name__ == "__main__":
    add_product("Iphone 16 Pro Max", "This is the most recent apple Iphone release.", 999.99)
    get_products()

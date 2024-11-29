# Product API
This project is a simple REST API built using Django and Django REST framework. The API allows you to manage a Product resource with fields for the name, description, and price of a product.

# Create and Activate a Virtual Environment
python -m venv .venv
.venv\Scripts\activate
# Install dependencies
pip install django djangorestframework
# Navigate to the Project Directory
cd Product_api
# Apply Database Migrations
python manage.py makemigrations 
python manage.py migrate
# Start the Development Server
python manage.py runserver
The server will start at http://127.0.0.1:8000/ but to access the Django REST framework go to http://127.0.0.1:8000/api/products/
# Using the Provided Python Script
python product_api_client.py
The script will:
Add a new product
Retrieve and print the list of all products
Delete a product with a specified ID (if modified for this)


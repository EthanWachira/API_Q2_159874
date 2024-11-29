from django.urls import path
from .views import ProductListCreate, home

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
]

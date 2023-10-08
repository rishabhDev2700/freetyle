from django.urls import path
from views import get_categories,get_category,get_products,get_product
app_name = "store"

urlpatterns = [
    path("/categories",get_categories,name="list_categories"),
    path("/category/<slug:name>",get_category,name="get_category"),
    path("/products",get_products,name="get_products"),
    path("/product/<slug:name>",get_product,name="get_product")
]
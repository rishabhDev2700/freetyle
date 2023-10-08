from django.shortcuts import get_object_or_404, render

from store.models import Category, Product

# Create your views here.
def get_categories(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request,"",context)

def get_category(request,name):
    try:
        category = Category.objects.filter(slug=name)
        products = Product.objects.filter(category=category)
    except(Exception):
        return render(request,"404.html")
    context={"category":category,"products":products}
    return render(request,"",context)    

def get_products(request):
    products = Product.objects.filter(visible=True)
    context = {"products":products}
    return render(request,"",context)

def get_product(request,name):
    try:
        product = Product.objects.get(slug=name)
    except Exception:
        return render(request,'404.html')
    context={"product":product}
    return render(request,"store/product.html",context)



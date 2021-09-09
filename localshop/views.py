from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Category, Product
from .serializers import ProductSerializer




def categories(request):
    return {
        'categories': Category.objects.all()
    }





def all_products(request):
    products = Product.products.all()
    return render(request, 'localshop/all_products.html', {'products': products})



def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'localshop/products/category_list.html', {'category':category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'localshop/products/product_detail.html', {'product': product})



class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






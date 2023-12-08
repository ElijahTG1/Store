from django.shortcuts import get_object_or_404, render #for loading templates
 
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all() #collecting all the category information to be returned
    }


def product_all(request): #taking in user request
    products = Product.products.all() #running a query on the product table and collecting all the data
    return render(request, 'store/home.html', {'products': products}) #gathering product data and loading the template to send back to the user


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


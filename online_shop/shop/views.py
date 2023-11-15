from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, slug=category_id)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/index.html', context)


def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, slug=category_id)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/products.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    context = {
        'product': product
    }
    return render(request, 'shop/single-product.html', context)

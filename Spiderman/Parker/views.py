from django.shortcuts import render, redirect
from .models import Product, Category, Brand, Review
# Create your views here.

def product_list(request):
    products = Product.objects.select_related('category', 'brand').all()
    
    return render(request, 'Parker/product_list.html', {'products': products})

def review_list(request):
    reviews = Review.objects.select_related('products', 'user').all()
    
    return render(request, 'Parker/review_list.html', {'reviews': reviews})

from django.shortcuts import render

# Create your views here.
def product_list(request):
    products = [
        
        {'name': 'Leather Bag', 'Price': 2000},
        {'name': 'Gucci', 'Price': 2200},
        {'name': 'Armani', 'Price': 3000},
        {'name': 'Air Force', 'Price': 4500},
    ]
    
    context = {'products': products}
    return render(request, 'kun/product_list.html', context)
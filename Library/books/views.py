from django.shortcuts import render
from .models import Author, Book
# Create your views here.

def home_page(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {'authors': authors, 'books': books}
    return render(request, 'books/home.html', context)
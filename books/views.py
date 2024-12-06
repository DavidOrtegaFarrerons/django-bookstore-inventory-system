from django.shortcuts import render

from .models import Book
from .services import fetch_books


def home(request):
    books = fetch_books()
    return render(request, 'home.html', {'books': books})

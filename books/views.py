from django.shortcuts import render

from .repositories.book_repository import BookRepository


def home(request):
    books = BookRepository.get_all_books_by_pub_date()
    return render(request, 'home.html', {'books': books})


def detail(request, book_id):
    book = BookRepository.get_book_by_id(book_id)
    return render(request, 'detail.html', {'book': book})

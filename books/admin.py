from typing import Any

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import Form
from django.http import HttpRequest
from unfold.admin import ModelAdmin

from .models import Author, Genre, Book
from .services import book_cover_exists_for_isbn, get_book_cover_for_isbn


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(ModelAdmin):
    def save_model(
            self, request: HttpRequest, obj: Book, form: Form, change: Any
    ) -> None:
        if book_cover_exists_for_isbn(obj.isbn):
            obj.book_cover = get_book_cover_for_isbn(obj.isbn)
            super().save_model(request, obj, form, change)
            return

        raise ValidationError("This isbn does not have a book cover.")

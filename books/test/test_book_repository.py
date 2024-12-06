from datetime import date

from django.test import TestCase

from books.models import Genre, Author, Book
from books.repositories.book_repository import BookRepository


class TestBookRepository(TestCase):
    def setUp(self):
        self.genre_fantasy = Genre.objects.create(name="Fantasy")
        self.genre_drama = Genre.objects.create(name="Drama")

        self.author_tom = Author.objects.create(
            name="Tom",
            birth_date=date(1980, 5, 14)
        )

        self.author_julia = Author.objects.create(
            name="Julia",
            birth_date=date(1997, 3, 24)
        )

        self.book__tom_fantasy = Book.objects.create(
            title="Fantasy book",
            author=self.author_tom,
            pub_date=date(2002, 4, 21),
            price=20.10
        )

        self.book__tom_fantasy.genres.add(self.genre_fantasy)

        self.book_julia_drama = Book.objects.create(
            title="Drama book",
            author=self.author_julia,
            pub_date=date(2022, 1, 12),
            price=20.11
        )

        self.book_julia_drama.genres.add(self.genre_drama)

    def test_get_all_books_by_pub_date(self):
        """
        Check that getting books by published date is ordered from newest to oldest
        """
        result = BookRepository.get_all_books_by_pub_date()
        expected_result = [self.book_julia_drama, self.book__tom_fantasy]
        self.assertQuerySetEqual(result, expected_result)


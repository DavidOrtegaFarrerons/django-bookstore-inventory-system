from books.models import Book


class BookRepository:

    @staticmethod
    def get_all_books_by_pub_date():
        return Book.objects.all().order_by("-pub_date")

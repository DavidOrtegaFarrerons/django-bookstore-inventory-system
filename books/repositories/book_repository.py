from books.models import Book


class BookRepository:

    @staticmethod
    def get_all_books_by_pub_date():
        return Book.objects.all().order_by("-pub_date")

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.get(pk=book_id)

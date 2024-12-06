from books.repositories.book_repository import BookRepository


def fetch_books():
    return BookRepository.get_all_books_by_pub_date()

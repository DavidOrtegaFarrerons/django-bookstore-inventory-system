import requests

OPEN_LIBRARY_BOOK_COVER = "https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"


def book_cover_exists_for_isbn(isbn: str) -> bool:
    """
    Checks if a book cover exists for a given isbn.
    """
    response = requests.get(get_book_cover_for_isbn(isbn))

    return response.status_code == 200


def get_book_cover_for_isbn(isbn: str) -> str:
    return f"{OPEN_LIBRARY_BOOK_COVER}".format(isbn=isbn)

class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def update_book(self, title, author, publication_date):
        book = self.get_book(title)
        if book:
            book.author = author
            book.publication_date = publication_date
            return True
        return False

    def delete_book(self, title):
        book = self.get_book(title)
        if book:
            self.books.remove(book)
            return True
        return False

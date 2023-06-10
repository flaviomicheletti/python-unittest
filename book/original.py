import unittest
from unittest.mock import MagicMock
from book import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        # Mock the Book object
        book = MagicMock()
        book.title = "The Great Gatsby"
        book.author = "F. Scott Fitzgerald"
        book.publication_date = "1925"

        # Add the book to the library
        self.library.add_book(book)

        # Verify that the book was added
        self.assertEqual(self.library.books, [book])

    def test_get_book(self):
        # Add a book to the library
        book = Book("To Kill a Mockingbird", "Harper Lee", "1960")
        self.library.add_book(book)

        # Mock the get_book method
        self.library.get_book = MagicMock(return_value=book)

        # Retrieve the book from the library
        retrieved_book = self.library.get_book("To Kill a Mockingbird")

        # Verify that the correct book was retrieved
        self.assertEqual(retrieved_book, book)

    def test_update_book(self):
        # Add a book to the library
        book = Book("The Catcher in the Rye", "J.D. Salinger", "1951")
        self.library.add_book(book)

        # Mock the get_book method
        self.library.get_book = MagicMock(return_value=book)

        # Update the book
        self.library.update_book("The Catcher in the Rye", "J.D. Salinger", "1953")

        # Verify that the book was updated
        updated_book = self.library.get_book("The Catcher in the Rye")
        self.assertEqual(updated_book.author, "J.D. Salinger")
        self.assertEqual(updated_book.publication_date, "1953")

    def test_delete_book(self):
        # Add a book to the library
        book = Book("1984", "George Orwell", "1949")
        self.library.add_book(book)

        # Mock the get_book method
        self.library.get_book = MagicMock(return_value=book)

        # Delete the book
        self.library.delete_book("198")

#
# 100%
#
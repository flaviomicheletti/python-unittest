import unittest
from unittest.mock import MagicMock
from book import Book, Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Title1", "Author1", "2023-01-01")
        self.library.add_book(self.book1)

    def test_add_book(self):

        # Test adding a book
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0], self.book1)

        # Test adding another book
        book2 = Book("Title2", "Author2", "2023-02-02")
        self.library.add_book(book2)
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[1], book2)

    def test_get_book_existing(self):
        # Test retrieving an existing book
        book = self.library.get_book("Title1")
        self.assertEqual(book, self.book1)

    def test_get_book_nonexistent(self):
        # Test retrieving a book that does not exist in the library
        book = self.library.get_book("Nonexistent Title")
        self.assertIsNone(book)

    def test_update_book_existing(self):
        # Test updating an existing book
        updated_author = "Updated Author"
        updated_publication_date = "2023-06-10"

        result = self.library.update_book(
            "Title1", updated_author, updated_publication_date)
        self.assertTrue(result)  # Check that update_book returns True

        # Check if the book attributes have been updated correctly
        book = self.library.get_book("Title1")
        self.assertEqual(book.author, updated_author)
        self.assertEqual(book.publication_date, updated_publication_date)

    def test_update_book_nonexistent(self):
        # Test updating a non-existent book
        updated_author = "Updated Author"
        updated_publication_date = "2023-06-10"

        result = self.library.update_book("Nonexistent Title", updated_author, updated_publication_date)
        # Check that update_book returns False
        self.assertFalse(result)

    def test_delete_book_existing(self):
        # Test deleting an existing book
        result = self.library.delete_book("Title1")
        self.assertTrue(result)  # Check that delete_book returns True

        # Check if the book has been removed from the library
        book = self.library.get_book("Title1")
        self.assertIsNone(book)

    def test_delete_book_nonexistent(self):
        # Test deleting a non-existent book
        result = self.library.delete_book("Nonexistent Title")
        # Check that delete_book returns False
        self.assertFalse(result)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author and some books for testing
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author,
        )

        # Set up URLs for testing
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})

    def test_list_books(self):
        """
        Ensure we can retrieve a list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        self.client.login(
            username="testuser", password="testpass"
        )  # Authenticate the user
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.pk,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """
        Ensure we can update an existing book.
        """
        self.client.login(
            username="testuser", password="testpass"
        )  # Authenticate the user
        data = {
            "title": "Harry Potter and the Sorcerer's Stone (Updated)",
            "publication_year": 1997,
            "author": self.author.pk,
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(
            self.book1.title, "Harry Potter and the Sorcerer's Stone (Updated)"
        )

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        self.client.login(
            username="testuser", password="testpass"
        )  # Authenticate the user
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """
        Ensure we can filter books by title.
        """
        response = self.client.get(
            self.list_url, {"title": "Harry Potter and the Sorcerer's Stone"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """
        Ensure we can search for books by title.
        """
        response = self.client.get(self.list_url, {"search": "Chamber"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """
        Ensure we can order books by publication_year.
        """
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["title"], "Harry Potter and the Sorcerer's Stone"
        )

    def test_permissions(self):
        """
        Ensure that unauthenticated users cannot create, update, or delete books.
        """
        data = {
            "title": "Harry Potter and the Goblet of Fire",
            "publication_year": 2000,
            "author": self.author.pk,
        }

        # Try creating a book without authentication
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Try updating a book without authentication
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Try deleting a book without authentication
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

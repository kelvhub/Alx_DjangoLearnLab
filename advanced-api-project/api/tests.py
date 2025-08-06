# api/tests.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITest(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=1960,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_publication_year(self):
        url = reverse('book-list') + '?publication_year=1958'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Ease'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "No Longer at Ease")

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 1960)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.pk])
        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": 1958,
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

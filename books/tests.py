from django.test import TestCase

from books.models import Book
# Create your tests here.
from django.urls import reverse


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No books found.")

    def test_books_list(self):
        Book.objects.create(title="Book1", description="description1", isbn="2342352")
        Book.objects.create(title="Book2", description="description2", isbn="2342452")
        Book.objects.create(title="Book3", description="description3", isbn="2342352")

        response = self.client.get(reverse("books:list"))
        books = Book.objects.all()

        for book in books:
            self.assertContains(response, book.title)

    def test_books_detail(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        response = self.client.get((reverse("books:detail", kwargs={"pk": book.id})))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)









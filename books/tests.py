from django.test import TestCase

from books.models import Book
# Create your tests here.
from django.urls import reverse


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No books found.")

    def test_books_list(self):
        book1 = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        book2 = Book.objects.create(title="Book2", description="description2", isbn="2342452")
        book3 = Book.objects.create(title="Book3", description="description3", isbn="2342352")

        response = self.client.get(reverse("books:list"))

        for book in [book1, book2]:
            self.assertContains(response, book.title)

        response = self.client.get(reverse("books:list") + '?page=2')
        self.assertContains(response, book3.title)

    def test_books_detail(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        response = self.client.get((reverse("books:detail", kwargs={"pk": book.id})))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)









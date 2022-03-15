from django.test import TestCase

from books.models import Book
# Create your tests here.
from django.urls import reverse

from users.models import CustomUser


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No books found.")

    def test_books_list(self):
        book1 = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        book2 = Book.objects.create(title="Book2", description="description2", isbn="2342452")
        book3 = Book.objects.create(title="Book3", description="description3", isbn="2342352")

        response = self.client.get(reverse("books:list") + '?page_size=2' )

        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + '?page=2&page_size=2')
        self.assertContains(response, book3.title)

    def test_books_detail(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        response = self.client.get((reverse("books:detail", kwargs={"id": book.id})))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_book(self):
        book1 = Book.objects.create(title="Sport", description="description1", isbn="2342352")
        book2 = Book.objects.create(title="Guide", description="description2", isbn="2342452")
        book3 = Book.objects.create(title="Shoe Dog", description="description3", isbn="2342352")

        response = self.client.get(reverse("books:list") + "?q=sport")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=guide")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=Shoe Dog")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        user = CustomUser.objects.create_user(username='shohijahon', email='shohijahon@gmail.com', password='admin@123', first_name='Shohijahon', last_name='Yodgorov')
        self.client.login(username='shohijahon', password='admin@123')

        self.client.post(reverse('books:reviews', kwargs={'id': book.id}), data={
            'stars_given': 3,
            'comment': "Nice",
        })

        book_reviews = book.bookreview_set.all()
        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, 'Nice')
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)

    def test_stars_given(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="2342352")
        user = CustomUser.objects.create_user(username='shohijahon', email='shohijahon@gmail.com', password='admin@123', first_name='Shohijahon', last_name='Yodgorov')
        self.client.login(username='shohijahon', password='admin@123')

        self.client.post(reverse('books:reviews', kwargs={'id': book.id}), data={
            'stars_given': 6,
            'comment': "Nice",
        })
        book_reviews = book.bookreview_set.all()
        self.assertEqual(book_reviews.count(), 0)











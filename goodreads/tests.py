from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn='1235325')
        user = CustomUser.objects.create(
            username='shohijahon',
            first_name='Shohijahon',
            last_name='Yodgorov',
            email='shohijahon@gmail.com',
        )
        user.set_password('somepass')
        user.save()
        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, comment='Very good')
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, comment='Useful book')
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='Very good book')

        response = self.client.get(reverse('home_page') + '?page_size=2')
        self.assertContains(response, review1.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review3.comment)

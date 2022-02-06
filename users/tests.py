from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse('users:register'), 
            data = {
                "username":"ali", 
                "first_name":"Alijon",
                'last_name':'Valiyev', 
                'email':'ali@gmail.com',
                'password': 'admin@123'
            }
        )
        user = User.objects.get(username="ali")

        self.assertEqual(user.first_name, "Alijon")
        self.assertEqual(user.last_name, 'Valiyev')
        self.assertEqual(user.email, 'ali@gmail.com')
        self.assertNotEqual(user.password, 'admin@123')
        self.assertTrue(user.check_password, 'admin@123')

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data = {
                'first_name': "Shohijahon",
                'last_name': "Yodgorov",
                "email": "shohijahon@gmail.com",
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')  # required fieldlarni tekshirish un
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse('users:register'), 
            data = {
                "username":"ali", 
                "first_name":"Alijon",
                'last_name':'Valiyev', 
                'email':'ali',
                'password': 'admin@123'
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        self.client.post(
            reverse('users:register'), 
            data = {
                "username":"vali", 
                "first_name":"Alijon",
                'last_name':'Valiyev', 
                'email':'ali@gmail.com',
                'password': 'admin@123'
            }
        )

        response = self.client.post(
            reverse('users:register'), 
            data={
                "username": "vali",
                "first_name": "Alijon",
                'last_name': 'Valiyev',
                'email': 'ali@gmail.com',
                'password': 'admin@123'
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')


class LoginTestCase(TestCase):
    def setUp(self):  # kodni takrorlamaslik un yozildi dry prinsipi
        self.db_user = User.objects.create(username='shoh')
        self.db_user.set_password('admin123')
        self.db_user.save()

    def test_successful_login(self):

        self.client.post(
            reverse('users:login'),
            data={
                'username': 'shoh',
                'password': 'admin123'
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):


        self.client.post(
            reverse('users:login'),
            data={
                'username': 'xatousername',
                'password': 'admin123'
            }
        )
        
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

        self.client.post(
            reverse('users:login'),
            data={
                'username': 'shoh',
                'password': 'xatoparol'
            }
        )
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

    def test_logout(self):

        self.client.login(

            username='shoh',
            password='admin123'

        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

        self.client.get(reverse('users:logout'))
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):

    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("users:login")+"?next=/users/profile/")

    def test_profile_details(self):
        user = User.objects.create(
            username="Kimdir",
            first_name="Kimdir",
            last_name="Kimdirov",
            email="kimdir@gmail.com",

        )
        user.set_password("somepass")
        user.save()
        self.client.login(username="Kimdir", password="somepass")
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)

        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

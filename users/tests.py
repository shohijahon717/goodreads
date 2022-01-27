from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


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
            data = {
                "username":"vali", 
                "first_name":"Alijon",
                'last_name':'Valiyev', 
                'email':'ali@gmail.com',
                'password': 'admin@123'
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')









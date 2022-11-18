
from django import forms
from django.core.mail import send_mail

from users.models import CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit) 
        user.set_password(self.cleaned_data["password"])
        user.save()
        if user.email:
            send_mail(
                "Goodreadsga xush kelibsiz!",
                f"Salom {user.username}. Goodreadsga xush kelibsiz!. Kitoblar va sharxlardan rohatlaning.",
                'shohijahonyodgorov2141@gmail.com',
                [user.email]
            )
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image']


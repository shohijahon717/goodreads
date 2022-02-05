from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.views import View
from .forms import UserCreateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                "form": create_form,
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {'login_form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        context = {'login_form': login_form}
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('landing_page')
        else:
            return render(request, 'users/login.html', context)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):

        context = {
            "user": request.user,
        }
        return render(request, "users/profile.html", context)

    def post(self, request):
        pass
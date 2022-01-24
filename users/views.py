from calendar import c
from time import process_time_ns
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
        return render(request, 'users/login.html')

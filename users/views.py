from django import views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.

class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()

        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, format=None):
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.warning(
                request,
                gettext('Correct the fields'),
            )

            return render(request, 'registration/login.html', {'form': form})

        try:
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('users:index')

            else:
                messages.warning(
                    request,
                    gettext('Username or Password is not correct'),
                )

            return render(request, 'registration/login.html', {'form': form})

        except:
            return render(request, 'registration/login.html', {'form': form})

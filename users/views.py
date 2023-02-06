from django import views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import LoginForm

# Create your views here.

decorators = [login_required]

class IndexView(views.View):
    def get(self, request, *args, **kwargs):
        return redirect('users:login')

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

            if user is not None and user.role == 1:
                login(request, user)
                return redirect('teacher:index')

            elif user is not None and user.role == 2:
                login(request, user)
                return redirect('student:index')

            else:
                messages.warning(
                    request,
                    gettext('Username or Password is not correct'),
                )

            return render(request, 'registration/login.html', {'form': form})

        except:
            return render(request, 'registration/login.html', {'form': form})

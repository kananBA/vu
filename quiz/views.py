from django.shortcuts import render, redirect
from django import views

from .models import Quiz
from .forms import QuizCreateForm

# Create your views here.


class QuizCreateView(views.View):
    def get(self, request, *args, **kwargs):
        form = QuizCreateForm()

        data = {
            'form': form,
        }

        return render(request, 'teacher/quiz-create.html', data)

    def post(self, request, format=None):
        form = QuizCreateForm(data=self.request.POST)

        if form.is_valid():
            form.save()

            return redirect('quiz:create')

        data = {
            'form': form,
        }

        return render(request, "teacher/quiz-create.html", data)

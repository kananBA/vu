from django.shortcuts import render, redirect
from django import views

from .models import Quiz, QuizMultipleChoiceQuestion
from .forms import QuizCreateForm, QuizMultipleChoiceCreateForm

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

class MultipleChoiceCreateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        quiz = Quiz.objects.get(id=pk)
        form = QuizMultipleChoiceCreateForm()
        multiple_choice_question_list = QuizMultipleChoiceQuestion.objects.filter(quiz=quiz)

        data = {
            'quiz': quiz,
            'form': form,
            'multiple_choice_question_list': multiple_choice_question_list,
        }

        return render(request, 'teacher/question-multiple-create.html', data)

    def post(self, request, pk=None, format=None):
        quiz = Quiz.objects.get(id=pk)
        form = QuizMultipleChoiceCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.quiz = quiz
            form.save()

            return redirect("quiz:multiple-choice-create", pk=quiz.id)

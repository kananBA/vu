from django import views
from django.shortcuts import render, redirect

from quiz.models import Quiz
from .models import MultipleChoiceQuestion, DescriptiveQuestion, FileQuestion
from .forms import MultipleChoiceQuestionCreateForm, DescriptiveQuestionCreateForm, FileQuestionCreateForm

# Create your views here.


class MultipleChoiceCreateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        quiz = Quiz.objects.get(id=pk)
        form = MultipleChoiceQuestionCreateForm()
        multiple_choice_question_list = MultipleChoiceQuestion.objects.filter(quiz=quiz)

        data = {
            'quiz': quiz,
            'form': form,
            'multiple_choice_question_list': multiple_choice_question_list,
        }

        return render(request, 'question/multiple-create.html', data)

    def post(self, request, pk=None, format=None):
        quiz = Quiz.objects.get(id=pk)
        form = MultipleChoiceQuestionCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.quiz = quiz
            form.save()

            return redirect("question:multiple-create", pk=quiz.id)


class DescriptiveCreateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        quiz = Quiz.objects.get(id=pk)
        form = DescriptiveQuestionCreateForm()
        descriptive_question_list = DescriptiveQuestion.objects.filter(quiz=quiz)

        data = {
            'quiz': quiz,
            'form': form,
            'descriptive_question_list': descriptive_question_list,
        }

        return render(request, 'question/descriptive-create.html', data)

    def post(self, request, pk=None, format=None):
        quiz = Quiz.objects.get(id=pk)
        form = DescriptiveQuestionCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.quiz = quiz
            form.save()

            return redirect("question:descriptive-create", pk=quiz.id)


class FileCreateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        quiz = Quiz.objects.get(id=pk)
        form = FileQuestionCreateForm()
        file_question_list = FileQuestion.objects.filter(quiz=quiz)

        data = {
            'quiz': quiz,
            'form': form,
            'file_question_list': file_question_list,
        }

        return render(request, 'question/file-create.html', data)

    def post(self, request, pk=None, format=None):
        quiz = Quiz.objects.get(id=pk)
        form = FileQuestionCreateForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            form.instance.quiz = quiz
            form.save()

            return redirect("question:file-create", pk=quiz.id)

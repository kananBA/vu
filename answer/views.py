from django import views
from django.shortcuts import render, redirect

from .models import MultipleChoiceAnswer, DescriptiveAnswer, FileAnswer
from .forms import MultipleChoiceAnswerUpdateForm, DescriptiveAnswerUpdateForm, FileAnswerUpdateForm

from quiz.models import QuizStudent

# Create your views here.


class AnswerUpdateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        quiz_student = QuizStudent.objects.get(id=pk)

        multiple_answer = MultipleChoiceAnswer.objects.filter(quiz_student=quiz_student, is_show=False).first()
        descriptive_answer = DescriptiveAnswer.objects.filter(quiz_student=quiz_student, is_show=False).first()
        file_answer = FileAnswer.objects.filter(quiz_student=quiz_student, is_show=False).first()

        if multiple_answer:
            return redirect("answer:multiple-update", pk=multiple_answer.id)

        elif descriptive_answer:
            return redirect("answer:descriptive-update", pk=descriptive_answer.id)

        elif file_answer:
            return redirect("answer:file-update", pk=file_answer.id)

        return render(request, 'answer/done.html', {})


class MultipleChoiceAnswerUpdateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        form = MultipleChoiceAnswerUpdateForm()

        multiple_answer = MultipleChoiceAnswer.objects.get(id=pk)
        multiple_answer.is_show = True
        multiple_answer.save()

        question = multiple_answer.question

        data = {
            'form': form,
            'question': question,
            'multiple_answer': multiple_answer,
        }

        return render(request, 'answer/multiple-detail.html', data)

    def post(self, request, pk=None, format=None):
        form = MultipleChoiceAnswerUpdateForm(self.request.POST)

        multiple_answer = MultipleChoiceAnswer.objects.get(id=pk)

        if form.is_valid():
            multiple_answer.answer = form.cleaned_data['answer']
            multiple_answer.save()

            return redirect("answer:answer-update", pk=multiple_answer.quiz_student.id)


class DescriptiveAnswerUpdateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        form = DescriptiveAnswerUpdateForm()

        descriptive_answer = DescriptiveAnswer.objects.get(id=pk)
        descriptive_answer.is_show = True
        descriptive_answer.save()

        question = descriptive_answer.question

        data = {
            'form': form,
            'question': question,
            'descriptive_answer': descriptive_answer,
        }

        return render(request, 'answer/descriptive-detail.html', data)

    def post(self, request, pk=None, format=None):
        form = DescriptiveAnswerUpdateForm(self.request.POST)

        descriptive_answer = DescriptiveAnswer.objects.get(id=pk)

        if form.is_valid():
            descriptive_answer.answer = form.cleaned_data['answer']
            descriptive_answer.save()

            return redirect("answer:answer-update", pk=descriptive_answer.quiz_student.id)


class FileAnswerUpdateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        form = FileAnswerUpdateForm()

        file_answer = FileAnswer.objects.get(id=pk)
        file_answer.is_show = True
        file_answer.save()

        question = file_answer.question

        data = {
            'form': form,
            'question': question,
            'file_answer': file_answer,
        }

        return render(request, 'answer/file-detail.html', data)

    def post(self, request, pk=None, format=None):
        form = FileAnswerUpdateForm(self.request.POST, self.request.FILES)

        file_answer = FileAnswer.objects.get(id=pk)

        if form.is_valid():
            file_answer.file = form.cleaned_data['file']
            file_answer.save()

            return redirect("answer:answer-update", pk=file_answer.quiz_student.id)

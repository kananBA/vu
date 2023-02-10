from django import views
from django.shortcuts import render, redirect

from quiz.models import Quiz, QuizStudent
from .models import MultipleChoiceQuestion, DescriptiveQuestion, FileQuestion
from .forms import MultipleChoiceQuestionCreateForm, DescriptiveQuestionCreateForm, FileQuestionCreateForm
from answer.models import MultipleChoiceAnswer, DescriptiveAnswer, FileAnswer

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
        student_list = quiz.course.student.all()
        form = MultipleChoiceQuestionCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.quiz = quiz
            multiple_choice_question = form.save()

            for student in student_list:
                quiz_student = QuizStudent.objects.get(quiz=quiz, student=student)
                MultipleChoiceAnswer.objects.create(
                    quiz_student=quiz_student,
                    question=multiple_choice_question,
                )

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
        student_list = quiz.course.student.all()
        form = DescriptiveQuestionCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.quiz = quiz
            descriptive_question = form.save()

            for student in student_list:
                quiz_student = QuizStudent.objects.get(quiz=quiz, student=student)
                DescriptiveAnswer.objects.create(
                    quiz_student=quiz_student,
                    question=descriptive_question,
                )

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
        student_list = quiz.course.student.all()
        form = FileQuestionCreateForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            form.instance.quiz = quiz
            file_question=form.save()

            for student in student_list:
                quiz_student = QuizStudent.objects.get(quiz=quiz, student=student)
                FileAnswer.objects.create(
                    quiz_student=quiz_student,
                    question=file_question,
                )

            return redirect("question:file-create", pk=quiz.id)

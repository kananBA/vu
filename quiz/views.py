from django.shortcuts import render, redirect
from django import views

from .models import QuizStudent
from .forms import QuizCreateForm
from course.models import Course

# Create your views here.


class QuizCreateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        form = QuizCreateForm()

        data = {
            'course': course,
            'form': form,
        }

        return render(request, 'teacher/quiz-create.html', data)

    def post(self, request, pk=None, format=None):
        course = Course.objects.get(id=pk)
        form = QuizCreateForm(data=self.request.POST)

        if form.is_valid():
            form.instance.course = course
            quiz = form.save()

            student_list = course.student.all()

            for student in student_list:
                QuizStudent.objects.create(
                    quiz=quiz,
                    student=student,
                )

            return redirect('quiz:create', pk=course.id)

        data = {
            'form': form,
        }

        return render(request, "teacher/quiz-create.html", data)

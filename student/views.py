from django import views
from django.shortcuts import render, redirect

from course.models import Course, CourseNotice
from task.models import CourseTask, CourseTaskStudent
from task.forms import TaskCreateForm
from quiz.models import QuizStudent

# Create your views here.


class DashboardTemplateView(views.View):
    def get(self, request, *args, **kwargs):
        student = self.request.user

        course_list = Course.objects.filter(student=student)

        data = {
            'course_list': course_list,
        }

        return render(request, 'student/dashboard.html', data)


class CourseTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)

        data = {
            'course': course,
        }

        return render(request, 'student/course.html', data)


class NoticeTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        course_notice_list = CourseNotice.objects.filter(course=course)

        data = {
            'course_notice_list': course_notice_list,
        }

        return render(request, 'student/notice.html', data)


class TaskListTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        course_task = CourseTask.objects.filter(course=course)

        data = {
            'course_task': course_task,
        }

        return render(request, 'student/task-list.html', data)


class TaskDetailTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        user = self.request.user
        course_task = CourseTask.objects.get(id=pk)

        course_task_student = CourseTaskStudent.objects.filter(course_task=course_task, student=user)
        form = TaskCreateForm()

        data = {
            'course_task_student': course_task_student,
            'form': form,
        }

        return render(request, 'student/task-detail.html', data)


class TaskCreateTemplateView(views.View):
    def post(self, request, pk=None, format=None):
        form = TaskCreateForm(self.request.POST, self.request.FILES)
        course_task_student = CourseTaskStudent.objects.get(id=pk)

        if form.is_valid():
            course_task_student.file = form.cleaned_data['file']
            course_task_student.save()

            return redirect("student:task-detail", pk=course_task_student.course_task.id)


class QuizListTemplateView(views.View):
    def get(self, request, format=None):
        user = self.request.user

        quiz_student_list = QuizStudent.objects.filter(student=user)

        data = {
            'quiz_list': quiz_student_list,
        }

        return render(request, 'student/quiz-list.html', data)

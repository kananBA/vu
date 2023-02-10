from django import views
from django.shortcuts import render, redirect

from course.forms import CourseUpdateForm, CourseNoticeCreateForm
from course.models import Course, CourseNotice

from users.models import User

# Create your views here.


class DashboardTemplateView(views.View):
    def get(self, request, *args, **kwargs):
        teacher = self.request.user

        course_list = Course.objects.filter(creator=teacher)

        data = {
            'course_list': course_list,
        }

        return render(request, 'teacher/dashboard.html', data)

class CourseTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        form = CourseUpdateForm(instance=course)

        data = {
            'course': course,
            'form': form,
        }

        return render(request, 'teacher/course.html', data)

    def post(self, request, pk=None, format=None):
        course = Course.objects.get(id=pk)
        form = CourseUpdateForm(self.request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect('teacher:course', pk=course.id)


class CourseStudentDeleteView(views.View):
    def get(self, request, pk=None, username=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        student = User.objects.get(username=username)

        course.student.remove(student)

        return redirect('teacher:course', pk=course.id)


class CourseStudentAddView(views.View):
    def get(self, request, pk=None, username=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        student = User.objects.get(username=username)

        course.student.add(student)

        return redirect('teacher:course', pk=course.id)


class CourseNoticeTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        form = CourseNoticeCreateForm()

        course = Course.objects.get(id=pk)
        course_notice_list = CourseNotice.objects.filter(course=course)

        data = {
            'course': course,
            'form': form,
            'course_notice_list': course_notice_list,
        }

        return render(request, 'teacher/notice.html', data)

    def post(self, request, pk=None, *args, **kwargs):
        form = CourseNoticeCreateForm(request.POST)

        course = Course.objects.get(id=pk)
        creator = self.request.user

        if form.is_valid():
            form.instance.course = course
            form.instance.creator = creator
            form.save()

        return redirect('teacher:notice', pk=course.id)


class CourseNoticeDeleteView(views.View):
    def get(self, request, pk=None, notice=None, *args, **kwargs):
        course = Course.objects.get(id=pk)

        course_notice = CourseNotice.objects.get(id=notice)
        course_notice.delete()

        return redirect('teacher:notice', pk=course.id)


class TaskDetailTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        return render(request, 'teacher/task-detail.html', {})


class TaskCreateTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        return render(request, 'teacher/task-create.html', {})

class TaskListTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        return render(request, 'teacher/task-list.html', {})

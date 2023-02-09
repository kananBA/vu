from django import views
from django.shortcuts import render

from course.models import Course

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

        data = {
            'course': course,
        }

        return render(request, 'teacher/course.html', data)

class CourseNoticeTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        return render(request, 'teacher/notice.html', {})

class TaskTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        return render(request, 'teacher/task.html', {})

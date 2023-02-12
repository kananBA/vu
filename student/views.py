from django import views
from django.shortcuts import render

from course.models import Course, CourseNotice

# Create your views here.


class DashboardTemplateView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'student/dashboard.html', {})


class NoticeTemplateView(views.View):
    def get(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(id=pk)
        course_notice_list = CourseNotice.objects.filter(course=course)

        data = {
            'course_notice_list': course_notice_list,
        }

        return render(request, 'student/notice.html', data)

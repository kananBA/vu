from django import views
from django.shortcuts import render

# Create your views here.


class DashboardTemplateView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'student/dashboard.html', {})

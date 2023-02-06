from django.urls import path

from .views import DashboardTemplateView

app_name = 'student'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
]

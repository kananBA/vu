from django.urls import path

from .views import DashboardTemplateView

app_name = 'teacher'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
]

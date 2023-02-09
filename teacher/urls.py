from django.urls import path

from .views import DashboardTemplateView, CourseTemplateView, CourseNoticeTemplateView, TaskTemplateView

app_name = 'teacher'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
    path('course/<int:pk>/', CourseTemplateView.as_view(), name='course'),
    path('notice/<int:pk>/', CourseNoticeTemplateView.as_view(), name='notice'),
    path('task/<int:pk>/', TaskTemplateView.as_view(), name='notice'),
]

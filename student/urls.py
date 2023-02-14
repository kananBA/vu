from django.urls import path

from .views import DashboardTemplateView, NoticeTemplateView, TaskListTemplateView, TaskDetailTemplateView, TaskCreateTemplateView, CourseTemplateView

app_name = 'student'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('course/<int:pk>/', CourseTemplateView.as_view(), name='course'),
    path('notice/<int:pk>/', NoticeTemplateView.as_view(), name='notice'),
    path('task/list/<int:pk>/', TaskListTemplateView.as_view(), name='task-list'),
    path('task/detail/<int:pk>/', TaskDetailTemplateView.as_view(), name='task-detail'),
    path('task/create/<int:pk>/', TaskCreateTemplateView.as_view(), name='task-create'),
]

from django.urls import path

from .views import DashboardTemplateView, CourseTemplateView, CourseNoticeTemplateView, TaskDetailTemplateView, TaskCreateTemplateView, TaskListTemplateView, CourseStudentDeleteView, CourseStudentAddView, CourseNoticeDeleteView

app_name = 'teacher'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
    path('course/<int:pk>/', CourseTemplateView.as_view(), name='course'),
    path('course/<int:pk>/student/delete/<str:username>/', CourseStudentDeleteView.as_view(), name='course-student-delete'),
    path('course/<int:pk>/student/add/<str:username>/', CourseStudentAddView.as_view(), name='course-student-add'),
    path('notice/<int:pk>/', CourseNoticeTemplateView.as_view(), name='notice'),
    path('notice/<int:pk>/delete/<int:notice>/', CourseNoticeDeleteView.as_view(), name='notice-delete'),
    path('task/create/<int:pk>/', TaskCreateTemplateView.as_view(), name='task-create'),
    path('task/list/<int:pk>/', TaskListTemplateView.as_view(), name='task-list'),
    path('task/detail/<int:pk>/', TaskDetailTemplateView.as_view(), name='task-detail'),
]

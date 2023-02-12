from django.urls import path

from .views import DashboardTemplateView, NoticeTemplateView

app_name = 'student'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
    path('notice/<int:pk>/', NoticeTemplateView.as_view(), name='index'),
]

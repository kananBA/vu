from django.urls import path

from .views import QuizCreateView

app_name = 'quiz'
urlpatterns = [
    path('create/<int:pk>/', QuizCreateView.as_view(), name='create'),
]

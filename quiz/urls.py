from django.urls import path

from .views import QuizCreateView, MultipleChoiceCreateView

app_name = 'quiz'
urlpatterns = [
    path('create/', QuizCreateView.as_view(), name='create'),
    path('multiple/create/<int:pk>/', MultipleChoiceCreateView.as_view(), name='multiple-choice-create'),
]

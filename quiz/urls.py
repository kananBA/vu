from django.urls import path

from .views import QuizCreateView, MultipleChoiceCreateView, DescriptiveCreateView

app_name = 'quiz'
urlpatterns = [
    path('create/', QuizCreateView.as_view(), name='create'),
    path('<int:pk>/multiple/create/', MultipleChoiceCreateView.as_view(), name='multiple-choice-create'),
    path('<int:pk>/descriptive/create/', DescriptiveCreateView.as_view(), name='descriptive-create'),
]

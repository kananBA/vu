from django.urls import path

from .views import MultipleChoiceAnswerUpdateView, DescriptiveAnswerUpdateView, FileAnswerUpdateView

app_name = 'question'
urlpatterns = [
    path('multiple/<int:pk>/', MultipleChoiceAnswerUpdateView.as_view(), name='multiple-update'),
    path('descriptive/<int:pk>/', DescriptiveAnswerUpdateView.as_view(), name='descriptive-update'),
    path('file/<int:pk>/', FileAnswerUpdateView.as_view(), name='file-update'),
]

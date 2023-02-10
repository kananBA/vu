from django.urls import path

from .views import MultipleChoiceCreateView, DescriptiveCreateView, FileCreateView

app_name = 'question'
urlpatterns = [
    path('<int:pk>/multiple/create/', MultipleChoiceCreateView.as_view(), name='multiple-create'),
    path('<int:pk>/descriptive/create/', DescriptiveCreateView.as_view(), name='descriptive-create'),
    path('<int:pk>/file/create/', FileCreateView.as_view(), name='file-create'),
]

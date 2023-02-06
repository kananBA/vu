from django.urls import path, include

from .views import LoginView, IndexView

app_name = 'users'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]

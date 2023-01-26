from django.urls import path, include

from .views import LoginView, DashboardTemplateView

app_name = 'users'
urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='index'),
    path('', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]

from django.urls import URLPattern, path
from . import views

app_name = 'monitor'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),     
]
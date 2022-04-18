from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path("neighbourhood/", views.createNeighbourHood, name = "neighbourhood"),
    path("newpost/", views.newPost, name = "newpost"),
    path("posts/", views.post, name = "post"),
    path("accounts/profile/", views.profile, name = "profile"),
    path("business/", views.business, name = "business"),

]

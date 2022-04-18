from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path("CreateNeighbourhood/", views.createNeighbourHood, name = "CreateNeighbourhood"),
    path("newPost/", views.new_post, name = "newpost"),
    path("posts/", views.post, name = "post"),
    path("accounts/profile/", views.profile, name = "profile"),
    path("business/", views.business, name = "business"),

]

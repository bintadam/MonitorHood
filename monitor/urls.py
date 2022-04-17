from django.urls import path
from .import views

app_name = 'monitor'

urlpatterns = [
    path('', views.home, name = 'home_page'),
    path("add_hood/", views.createNeighbourHood, name = "add_hood"),
    path("new_post/", views.newPost, name = "new_post"),
    path("posts/", views.post, name = "post"),
    path("accounts/profile/", views.profile, name = "profile"),
    path("business/", views.business, name = "business"),
    path("logout/", views.logout, name = "logout"),
]
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'monitor'

urlpatterns = [
    path('', views.home, name = 'home'),
    path("accounts/profile/", views.profile, name = "profile"),
    path("neighbourhood/", views.createNeighbourHood, name = "neighbourhood"),
    path("newPost/", views.newPost, name = "newPost"),
    path("posts/", views.post, name = "post"),
    # path("accounts/profile/", views.profile, name = "profile"),
    path("business/", views.business, name = "business"),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
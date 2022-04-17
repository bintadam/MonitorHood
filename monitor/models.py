from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length=60, null=True)
    image = CloudinaryField('image')
    user = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, null=True)
    location = models.CharField(max_length=200, null=True)
    population = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    def create_neighbour(self):
        self.save()

    def delete_neighbour(self):
        self.delete()

    @classmethod
    def find_neighbour(cls, id):
        jirani = cls.objects.get(id = id)
        return jirani

    def update_neighbour(self, name):
        self.name = name
        self.save()

class Post(models.Model):
    title = models.CharField(max_length=255)
    neighbourhood= models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    image = CloudinaryField('image')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, blank=True)
    image = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbour, on_delete=models.SET_NULL, null=True, related_name='users')


    def __str__(self):
        return f'{self.user.username} profile'



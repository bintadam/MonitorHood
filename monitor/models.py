from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length=60, null=True)
    image = CloudinaryField('image')
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


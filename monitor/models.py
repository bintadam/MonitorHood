from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    neighbour= models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    image = CloudinaryField('image')


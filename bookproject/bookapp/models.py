from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class RegisterBook(models.Model):
    photo = models.ImageField(upload_to="images", default="none")
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def coverphoto(self):
        return mark_safe(f'<img src="{self.photo.url}" width="100px"/')

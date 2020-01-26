from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=50)
    content = models.TextField(max_length=3000)
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    liked = models.IntegerField(default=0)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='articles')

    def __str__(self):
        return self.header
    
class Comment(models.Model):
    header = models.CharField(max_length=30)
    content = models.TextField(max_length=280)
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='comments')
    
    def __str__(self):
        return f"{self.header}'e demisler ki"
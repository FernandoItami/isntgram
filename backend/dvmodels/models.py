from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import date, datetime


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    description  = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    #post_image = models.ImageField()
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes")
    
    def __str__(self):
        return self.description + ' | ' + str(self.author)
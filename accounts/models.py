from django.contrib.auth.models import User
from django.db import models



class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Item', related_name='favorited_by', blank=True)

    def __str__(self):
        return self.user.username

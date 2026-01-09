from django.db import models


class Users(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=225)
    objects = None

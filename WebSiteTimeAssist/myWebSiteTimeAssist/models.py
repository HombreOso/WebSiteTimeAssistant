from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class UserCredentials(models.Model):
    nickname = CharField(max_length=100)
    password = CharField(max_length=100)
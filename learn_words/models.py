from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    english_name = models.CharField(max_length=100)
    translated_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='words_image', blank=True)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_picture = models.ImageField(upload_to='account_picture', blank=True)
    vocabulary = models.ManyToManyField(Words)

from django.db import models


class Dog(models.Model):
    nickname = models.CharField(max_length=50)
    slug = models.SlugField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)


class Breed(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

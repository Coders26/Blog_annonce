from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class First(models.Model):
    titre = models.CharField(max_length= 50)
    contenus = models.TextField()

    def __str__(self):
        return self.titre

class Second(models.Model):
    titre = models.CharField(max_length= 50)
    contenus = models.TextField()

    def __str__(self):
        return self.titre


class Third(models.Model):
    titre = models.CharField(max_length=50)
    contenus = models.TextField()

    def __str__(self):
        return self.contenus


class Fourth(models.Model):
    titre = models.CharField(max_length=50)
    contenus = models.TextField()

    def __str__(self):
        return self.contenus

class Plus(models.Model):
    lien = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.lien

class Info(models.Model):
    number = models.TextField()
    mail = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.number

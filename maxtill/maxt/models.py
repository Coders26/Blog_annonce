from django.db import models

# Create your models here.

class Title(models.Model):
    titre = models.CharField(max_length= 50)

    def __str__(self):
        return self.titre

class First(models.Model):
    titre = models.CharField(max_length= 150)
    contenus = models.TextField()

    def __str__(self):
        return self.titre


class Second(models.Model):
    contenus = models.TextField()

    def __str__(self):
        return self.contenus


class Third(models.Model):
    contenus = models.TextField()

    def __str__(self):
        return self.contenus

class Info(models.Model):
    number = models.TextField()
    mail = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.number
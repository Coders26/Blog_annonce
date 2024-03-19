from django.db import models
import datetime

# Create your models here.

class Info(models.Model):
    number = models.TextField()
    mail = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.number

class Annonce(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    contenu = models.TextField()


    def __str__(self):
        return self.title

class Commentaire(models.Model):
    nom = models.CharField(max_length=150)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='commentaire')
    commentaire = models.TextField()

    # Standards
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.nom

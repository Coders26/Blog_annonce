from django.db import models

# Create your models here.
class Info(models.Model):
    number = models.TextField()
    mail = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.number

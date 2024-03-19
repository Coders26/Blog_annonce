from django.db import models

# Create your models here.
class Message(models.Model):
    contenus = models.TextField()

    def __str__(self):
        return self.contenus

class Info(models.Model):
    number = models.TextField()
    mail = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.number

class Contact(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField()
    contenus = models.TextField()
    active= models.BooleanField(default=False)

    # standard
    statuts = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_add']

    def __str__(self):
        return 'Contact {} by {}'.format(self.contenus, self.nom)




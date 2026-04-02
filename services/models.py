from django.db import models

# Create your models here.
class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=100)
    specialites = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=200)
    est_actif = models.BooleanField(default=True)
    email = models.EmailField()
    datedecreation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='traiteurs/', blank=True, null=True)

    def __str__(self):
        return self.nomcomplet
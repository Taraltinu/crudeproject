from django.db import models

# Create your models here.

class RegModel(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    zips = models.IntegerField()
    def __str__(self):
        return self.city

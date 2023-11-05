from django.db import models

# Create your models here.


class Shops(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    sells= models.CharField(max_length=100)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_OpenSundays = models.BooleanField(default=True)

  

    def __str__(self):
        return self.name
from django.db import models


# Create your models here.
class Greeting(models.Model):
    greeting = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


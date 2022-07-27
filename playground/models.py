from django.db import models
# Migrate after making changes to any models.py


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=30, blank=True)  # Blank means it's a required field.
    description = models.TextField(blank=False, null=True)  # Null means
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    summary     = models.TextField(default='A product created in the playground.')
    featured    = models.BooleanField()  # When appending models, null=True or default=True

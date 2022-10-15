from django.db import models

# Create your models here.
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    RAM = models.IntegerField()
    memory = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.CharField(max_length=255)
    def __str__(self):
        return self.name
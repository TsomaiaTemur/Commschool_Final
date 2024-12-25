from django.db import models

# Create your models here.
class Toy(models.Model):
    toy_type = models.CharField(max_length=50)

class Coal(models.Model):
    name = 'Coal'

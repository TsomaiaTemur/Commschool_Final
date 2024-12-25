from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Kid(models.Model):
    name = models.CharField(max_length=50)
    niceness_coefficient = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    gift = models.OneToOneField(
        'Toy_factory.Toy',  # Replace 'other_app' with the actual name of the app containing the Toy model
        on_delete=models.CASCADE,  # Specifies behavior when the referenced Toy is deleted
        related_name='kids'  # Optional: Allows reverse lookup from Toy to its related Kids
    )

class Santas_list(models.Model):
    naughty_list = models.ManyToManyField()
    nice_list = models.ManyToManyField()

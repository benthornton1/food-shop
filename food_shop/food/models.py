from django.db import models

# Create your models here.

class Food(models.Model):
    grams = 'g'
    single = 'single'
    kilograms = 'kg'
    milliliters = 'ml'
    liters = 'l'
    UNIT_CHOICES = (
        (grams, 'Grams'),
        (single, 'Single'),
        (kilograms, 'Kilograms'),
        (milliliters, 'Milliliters'),
        (liters, 'Liters'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    unit = models.CharField(max_length = 200, choices = UNIT_CHOICES, default=grams)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img', blank=True)

    def __str__(self):
        return self.name

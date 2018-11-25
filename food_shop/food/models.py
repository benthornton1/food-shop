from django.db import models

# Create your models here.

class Food(models.Model):
    grams = 'g'
    single = 'unit'
    kilograms = 'kg'
    milliliters = 'ml'
    liters = 'l'
    UNIT_CHOICES = (
        (grams, 'Grams'),
        (single, 'Unit'),
        (kilograms, 'Kilograms'),
        (milliliters, 'Milliliters'),
        (liters, 'Liters'),
    )
    meat = 'Meat'
    dairy = 'Dairy'
    baking = 'Baking'
    poultry = 'Poultry'
    CATEGORY_CHOICES = (
        (meat, 'Meat'),
        (dairy, 'Dairy'),
        (baking, 'Baking'),
        (poultry, 'Poultry'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length = 200, choices = CATEGORY_CHOICES, default=meat)
    price = models.DecimalField(decimal_places=10, max_digits=20)
    stock = models.PositiveIntegerField()
    unit = models.CharField(max_length = 200, choices = UNIT_CHOICES, default=grams)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food:food_detail', args=[self.food_id])

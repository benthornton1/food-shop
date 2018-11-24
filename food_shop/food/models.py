from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='food/food_img', blank=True)

    def __str__(self):
        return self.name

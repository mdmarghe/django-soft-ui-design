from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='wines/', null=True, blank=True)
    production_house = models.CharField(max_length=100)
    grape_variety = models.CharField(max_length=100)
    denomination_of_origin = models.CharField(max_length=100)
    quantity_available = models.PositiveIntegerField(default=0)
    # Other fields as needed

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wines = models.ManyToManyField(Wine, through='OrderedWine')
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



class OrderedWine(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.wine.quantity_available -= self.quantity
        self.wine.save()



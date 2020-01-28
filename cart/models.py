from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from food.models import Dishes

class Cart(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

class CartItem(models.Model):
    Dishes = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def price_ttc(self):
        return self.price_ht
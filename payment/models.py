

from django.db import models
from product.models import Product,Cart
from django.contrib.auth.models import User


class Checkout(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
  

    def __str__(self):
        return f"Order for {self.name} (x{self.quantity})"
         

class Orderitem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1) 
    status = models.CharField(max_length=20, choices=[
        ('success', 'Success'), 
        ('failed', 'Failed'), 
        ('pending', 'Pending')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order ({self.product_name})"

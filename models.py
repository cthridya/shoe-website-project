from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEOGRY_CHOICES=(
    ('M','Men'),
    ('W','Women'),
    ('K','Kids'),

)

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='media')
    cateogry=models.CharField(choices=CATEOGRY_CHOICES,max_length=2)
    
    def __str__(self):
        return self.product_name
class AddtoCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    options=(
    
        ("order-placed","order-placed"),
        ("dispatched",'dispatched'),
        ("cancelled,cancelled")
    )
    status=models.CharField(max_length=200,)
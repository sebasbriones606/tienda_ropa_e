from django.db import models
from django.shortcuts import render
from .models import Product

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    stock_quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    # Otros campos relevantes
    

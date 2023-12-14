from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        ordering = ['name']
        
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_stars = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    product_feedback = models.TextField()


    def __str__(self):
        return self.product_name

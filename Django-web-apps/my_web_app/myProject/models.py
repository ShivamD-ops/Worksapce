from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_sallary = models.CharField(max_length = 100,default="0")
    emp_feedback = models.TextField()


    def __str__(self):
        return self.emp_name

# class ProductModel(models.Model):
#     product_name = models.CharField(max_length=200)
#     product_category = models.CharField(max_length=200)
#     product_stars = models.IntegerField(default=0)
#     product_price = models.IntegerField(default=0)
#     product_feedback = models.TextField()


#     def __str__(self):
#         return self.product_name







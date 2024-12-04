from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = EmployeeModel
        fields = [
            'emp_name',
            'emp_sallary',
            'emp_feedback'
        ]

# class ProductForm(forms.ModelForm):

#     class Meta:
#         model = ProductModel
#         fields = [
#             'product_name',
#             'product_category', 
#             'product_stars' ,
#             'product_price', 
#             'product_feedback' 
#         ]
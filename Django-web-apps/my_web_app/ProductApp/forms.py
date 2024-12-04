from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = [
            'product_name',
            'product_category', 
            'product_stars' ,
            'product_price', 
            'product_feedback' 
        ]
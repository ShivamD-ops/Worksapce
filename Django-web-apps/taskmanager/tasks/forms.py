'''
created by-> Shivam Devaser
on-> 5-12-2024
This file contains Task Form and fields to be loaded 

'''
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'completed'
        ]


'''
created by-> Shivam Devaser
on-> 5-12-2024

'''
from django.db import models

# Create your models here.

# Task Model
class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    completed = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

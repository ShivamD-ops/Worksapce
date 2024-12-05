"""
Created by -> SHIVAM DEVASER
on-> 05-12-2024

this file changes->
1) added tasks url
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("tasks.urls")), # include path to tasks urls
]

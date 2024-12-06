"""
created by - > SHIVAM DEVASER
on-> 5-12-2024

added tasks.urls

"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include('tasks.urls'))
]

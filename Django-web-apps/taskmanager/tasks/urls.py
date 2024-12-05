'''
created by-> Shivam Devaser
on-> 5-12-2024
This file contains different paths of url and the view method to be triggered 

'''
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.all_task_list),
    path('create/',views.create_new_task),
    path('detail_task/<id>',views.task_detail_view),
    path('update_task/<id>',views.task_update_view),
    path('delete_task/<id>',views.task_delete_view),
]


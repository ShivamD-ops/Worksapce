# from django.conf.urls import urls
'''
Created by -> Shivam Devaser
on - > 5-12-2024

created urls ->
re_path(r'^api/tasks$',views.tasks_list), -> Get and Post
re_path(r'^api/tasks/(?P<pk>[0-9]+)$',views.tasks_details), -> Get,Put and Delete

'''
from django.urls import path,re_path
from tasks import views

urlpatterns = [
    re_path(r'^api/tasks$',views.tasks_list),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)$',views.tasks_details),
    # path('api/validate/',views.validate_user)
]
# from django.conf.urls import urls
from django.urls import path,re_path
from tasks import views

urlpatterns = [
    re_path(r'^api/tasks$',views.tasks_list),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)$',views.tasks_details),
    # path('api/validate/',views.validate_user)
]
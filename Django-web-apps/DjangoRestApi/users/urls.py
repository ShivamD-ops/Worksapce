# from django.conf.urls import urls
from django.urls import path,re_path
from users import views

urlpatterns = [
    re_path(r'^api/users$',views.user_list),
    re_path(r'^api/users/(?P<pk>[0-9]+)$',views.user_details),
    path('api/validate/',views.validate_user)
]
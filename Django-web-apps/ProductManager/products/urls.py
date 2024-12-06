# from django.conf.urls import urls
from django.urls import path,re_path
from products import views

urlpatterns = [
    re_path(r'^products$',views.product_list),
    re_path(r'^products/(?P<pk>[0-9]+)$',views.product_details),
    re_path(r'^products/(?P<pk>[0-9]+)/total',views.product_total)
    # path('api/validate/',views.validate_user)
]
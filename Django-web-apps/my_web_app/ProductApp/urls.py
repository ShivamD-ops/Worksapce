from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create_product/',views.create_view_product),
    path('list_product/',views.list_view_product),
    path('detail_list_product/<id>',views.detail_view_product),
    path('update_product/<id>',views.update_view_product),
    path('delete_product/<id>',views.delete_view_product),
]


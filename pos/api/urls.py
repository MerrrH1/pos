from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    TableRestoListApiView, TableRestoDetailApiView, CategoryListApiView, CategoryDetailApiView, 
    MenuRestoListApiView, MenuRestoDetailApiView, OrderMenuListApiView, OrderMenuDetailApiView
)

app_name = 'api'

urlpatterns = [
    path('api/table_resto', views.TableRestoListApiView.as_view()),
    path('api/table_resto/<int:id>', views.TableRestoDetailApiView.as_view()),
    path('api/category', views.CategoryListApiView.as_view()),
    path('api/category/<int:id>', views.CategoryDetailApiView.as_view()),
    path('api/menu_resto', views.MenuRestoListApiView.as_view()),
    path('api/menu_resto/<int:id>', views.MenuRestoDetailApiView.as_view()),
    path('api/order_menu', views.OrderMenuListApiView.as_view()),
    path('api/order_menu/<int:id>', views.OrderMenuDetailApiView.as_view()),
    path('api/order_menu_detail', views.OrderMenuDetailListApiView.as_view()),
    path('api/order_menu_detail/<int:id>', views.OrderMenuDetailDetailDetailApiView.as_view()),
]
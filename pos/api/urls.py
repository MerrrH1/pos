from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    CategoryListApiView
)

app_name = 'api'

urlpatterns = [
    path('api/category', views.CategoryListApiView.as_view()),
    path('api/category/<int:id>', views.CategoryDetailApiView.as_view()),
]
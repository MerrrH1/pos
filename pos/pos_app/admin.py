from django.contrib import admin
from pos_app.models import (
    User, StatusModel, Category, 
    OrderMenuDetail, MenuResto, OrderMenu, Profile, TableResto
)

admin.site.register(User)
admin.site.register(StatusModel)
admin.site.register(Category)
admin.site.register(OrderMenuDetail)
admin.site.register(MenuResto)
admin.site.register(OrderMenu)
admin.site.register(Profile)
admin.site.register(TableResto)
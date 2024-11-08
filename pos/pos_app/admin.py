from django.contrib import admin
from pos_app.models import User, TableResto, Profile, Category, MenuResto

admin.site.register(User)
admin.site.register(TableResto)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(MenuResto)
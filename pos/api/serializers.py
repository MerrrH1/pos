from rest_framework import serializers
from pos_app.models import (
    User, Category, StatusModel, Profile, TableResto,
    OrderMenuDetail, MenuResto, OrderMenu
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class StatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TableRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableResto
        fields = '__all__'

class MenuRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuResto
        fields = ('code', 'name', 'price', 'description', 'image_menu', 'menu_status', 'status')

class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = "__all__"

class OrderMenuDetailSerializer(serializers.ModelSerializer):
    model = OrderMenuDetail
    fields = "__all__"
from rest_framework import serializers
from pos_app.models import (
    User, TableResto, MenuResto
)

class TableRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableResto
        fields = ('code', 'name', 'capacity', 'table_status', 'status')
        # fields = "__all__"

class MenuRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuResto
        fields = ('code', 'name', 'category', 'price', 'status')
        # fields = "__all__"
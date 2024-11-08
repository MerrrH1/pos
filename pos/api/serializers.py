from rest_framework import serializers
from pos_app.models import (
    User, TableResto, MenuResto
)

class TableRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableResto
        fields = ('id', 'code', 'name', 'capacity', 'table_status', 'status')
        # fields = "__all__"

class MenuRestoSerializer(serializers.Serializer):
    class Meta:
        model = MenuResto
        fields = ('id', 'code', 'price', 'name', 'category')
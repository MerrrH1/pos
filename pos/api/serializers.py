from rest_framework import serializers
from pos_app.models import (
    User, TableResto
)

class TableRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableResto
        fields = ('id', 'code', 'name', 'capacity', 'table_status', 'status')
        # fields = "__all__"
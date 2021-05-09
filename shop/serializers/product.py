from rest_framework import serializers
from ..models import Product
from ..models import User


class ProductSerializer(serializers.ModelSerializer):

    added_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, read_only=True)

    def create(self, validated_data):
        tenant = self.context['request'].tenant
        added_by = self.context['request'].user
        validated_data.update(**{
            'tenant': tenant,
            'added_by': added_by
        })
        return Product.objects.t_filter(tenant=tenant).create(**validated_data)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'code',
            'added_on',
            'added_by'
        ]

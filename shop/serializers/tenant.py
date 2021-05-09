from rest_framework import serializers

from ..models import Tenant


class TenantSerializer(serializers.ModelSerializer):

    def validate(self, data):
        code = data.get('code', '')
        for each_code_char in code:
            if each_code_char == ' ' or each_code_char.isupper():
                raise serializers.ValidationError({
                    'code': [
                        'Code should be lowercase and without spaces'
                    ]
                })
        return data

    def create(self, validated_data):
        return Tenant.objects.create(**validated_data)

    class Meta:
        model = Tenant
        fields = [
            'id',
            'name',
            'code'
        ]


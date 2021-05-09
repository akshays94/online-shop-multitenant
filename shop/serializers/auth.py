from rest_framework import serializers

from ..models import User

class RegisterUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tenant = self.context['request'].tenant
        user = User.user_objects.create_user(
            validated_data['email'],
            validated_data['password'], **{
                'first_name': validated_data.get('first_name'),
                'last_name': validated_data.get('last_name'),
                'tenant': tenant
            })
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            # 'auth_token'
        )
        # read_only_fields = ('auth_token',)
        # extra_kwargs = {'password': {'write_only': True}}
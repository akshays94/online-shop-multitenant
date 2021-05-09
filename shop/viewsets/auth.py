from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from ..serializers.auth import RegisterUserSerializer
from ..serializers.user import UserSerializer

from knox.models import AuthToken


class AuthViewSet(viewsets.GenericViewSet):

    @action(
        url_path='register',
        methods=['post'],
        detail=False,
        permission_classes=[AllowAny])
    def register_user(self, request):
        serializer = RegisterUserSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token[1]
        })

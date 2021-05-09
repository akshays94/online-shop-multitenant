from rest_framework import exceptions
from knox.auth import TokenAuthentication
from ..models import User


class CustomTokenAuthentication(TokenAuthentication):

    def authenticate(self, request):
        user, auth_token = super().authenticate(request)

        if user.tenant != request.tenant:
            raise exceptions.AuthenticationFailed(
                'User does not exist in this tenant')

        return user, auth_token

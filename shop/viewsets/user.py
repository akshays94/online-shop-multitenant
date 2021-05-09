from rest_framework import viewsets
from ..serializers.user import UserSerializer
from ..models import User
from ..authentication.auth import CustomTokenAuthentication


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    authentication_classes = (CustomTokenAuthentication, )
    pagination_class = None

    def get_queryset(self):
        return User.objects \
            .t_filter(tenant=self.request.tenant) \
            .order_by('first_name')

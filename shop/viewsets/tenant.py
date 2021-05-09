from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from ..serializers.tenant import TenantSerializer
from ..models import Tenant


class TenantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    serializer_class = TenantSerializer
    queryset = Tenant.objects.all().order_by('name')
    permission_classes = [AllowAny]
    pagination_class = None

from rest_framework import viewsets
from ..models import Product
from ..serializers.product import ProductSerializer
from ..authentication.auth import CustomTokenAuthentication


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    authentication_classes = (CustomTokenAuthentication, )
    pagination_class = None

    def get_queryset(self):
        return Product.objects \
            .t_filter(tenant=self.request.tenant) \
            .order_by('code')

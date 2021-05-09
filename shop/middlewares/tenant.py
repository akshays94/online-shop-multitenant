from django.http import Http404
from django.urls import reverse

from ..models import Tenant

TENANT_URLS = [
    reverse('tenants-list')
]

class CustomTenantMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.TENANT_NOT_FOUND_EXCEPTION = Http404

    def __call__(self, request):
        code = request.META.get('HTTP_TENANT_CODE')
        if request.path in TENANT_URLS:
            return self.get_response(request)
        try:
            tenant = Tenant.objects.get(code=code)
            request.tenant = tenant
            return self.get_response(request)
        except Exception:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                f'Tenant with code \'{code}\' does not exists'
            )

from django.db import models


class TenantManager(models.Manager):

    def get_queryset(self):
        return None

    def t_filter(self, tenant, **kwargs):
        return super(TenantManager, self) \
            .get_queryset() \
            .filter(tenant=tenant, **kwargs)

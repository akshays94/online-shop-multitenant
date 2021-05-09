import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers.tenant import TenantManager
from .managers.user import CustomUserManager


class Tenant(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128, unique=True)


class TenantBaseModel(models.Model):

    class Meta:
        abstract = True
    
    objects = TenantManager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)


class User(AbstractBaseUser, TenantBaseModel):

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = list()

    objects = TenantManager()
    user_objects = CustomUserManager()
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512, null=True, blank=True)
    email = models.EmailField(max_length=512)

    class Meta:
        unique_together = ('tenant_id', 'email',)


class Product(TenantBaseModel):

    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

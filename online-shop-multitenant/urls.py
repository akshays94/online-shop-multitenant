from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from .users.views import UserViewSet, UserCreateViewSet

from shop.viewsets.tenant import TenantViewSet
from shop.viewsets.auth import AuthViewSet
from shop.viewsets.user import UserViewSet
from shop.viewsets.product import ProductViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenants')
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'users', UserViewSet, basename='users')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

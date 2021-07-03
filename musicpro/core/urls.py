from django import urls
from django.urls import path
from django.urls.conf import include
from productos.views import ProductViewSet
from rest_framework import routers

# Create your views here.
router = routers.DefaultRouter()
router.register('productos', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
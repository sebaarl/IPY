from django.contrib import admin
from django.urls.conf import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from productos.views import ProductViewSet
from rest_framework import routers

# Create your views here.
router = routers.DefaultRouter()
router.register('productos', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('cart/', include('cart.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
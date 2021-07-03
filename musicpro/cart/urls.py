from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('shop/', views.ProductListView.as_view(), name='product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('carro-compras/', views.CartView.as_view(), name='summary'),
    path('aumentar-cantidad/<pk>/', views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('reducir-cantidad/<pk>/', views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
    path('remover-de-carro/<pk>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
]  
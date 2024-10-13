from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, CustomerViewSet, SecureView
from . import views

router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
urlpatterns = [
  path('products/search/',views.ProductSearchView.as_view(),name ='product-search'),
  path('', include(router.urls)),
  path('secure/', SecureView.as_view(),name='secure_endpoint'),
 ]
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Category, Product,Orders,Customer
from .serializers import CategorySerializer, OrderSerializer, ProductSerializer, CustomerSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permisions import IsAdminorVendor

class ProductCreateView(APIView):
    permission_classes = [IsAdminorVendor,IsAuthenticated]
    def post(self, request):
        return Response({'message': 'Product created successfully'})

class SecureView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'message:This is a secure endpoint'})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductSearchView(ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends =[SearchFilter,DjangoFilterBackend]
    search_fields = ['name', 'category_name']
    filterset_fields= ['category']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Create your views here.

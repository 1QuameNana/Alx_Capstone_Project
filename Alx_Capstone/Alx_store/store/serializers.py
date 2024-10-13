from rest_framework import serializers
from .models import Product, Customer, Orders, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['id', 'name','description']
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name',
                  'category','stock',
                  'description','image_URL',
                  'Created_date'
                  ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','user',
                  'address','phone_number'
                  ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields =['id', 'customer',
                 'quantity','order_date',
                 'status','product'
                 ]

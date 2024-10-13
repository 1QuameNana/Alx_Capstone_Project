from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, null =True, blank=True)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index= True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    description = models.TextField()
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    stock =models.PositiveIntegerField()
    image_URL =models.URLField(max_length=200,blank=True, null =True )
    Created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   address = models.TextField()
   phone_number = models.CharField(max_length=20)

   def __str__(self):
       return self.user.username
   
class Orders(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending','Pending'),
                                                      ('Shipped','Shipped'),
                                                      ('Delivered','Delivered')])
    
    def __str__(self):
        return f'Order{self.id} by {self.Customer}'

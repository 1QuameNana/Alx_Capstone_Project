from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('User must have an email')
        email =self.normalize_email(email)
        if not username:
            raise ValueError('user must have a username')
        user =self.model(email= email,username=username)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def create_superuser(self, email, username,password):

        user = self.create_user(email,username,password)

        user.is_staff =True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

class User(AbstractUser):
    ROLE_CHOICES =(
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'CUstomer'),
    )
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='customer')
    email = models.EmailField(verbose_name='email address', max_length=20, unique=True)
    username = models.CharField(max_length=20, unique= False)
    date_joined =models.DateTimeField(auto_now_add= True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects= UserManager()
    def __str__(self):
        return self.username


    

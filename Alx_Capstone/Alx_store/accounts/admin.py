from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUser
from .models import User

class CustomUserAdmin(CustomUser):
    list_display =('email','is_staff','is_active','username')

admin.site.register(User,CustomUserAdmin)


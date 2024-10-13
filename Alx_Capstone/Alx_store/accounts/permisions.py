from rest_framework.permissions import BasePermission

class IsAdminorVendor(BasePermission):
    def has_permision(self,request,view):
        return request.user.is_authenticated and request.user.role in ['admin','vendor']

from rest_framework.permissions import BasePermission

# permisos administrador
class IsAdminOrReadOnly(BasePermission):
     def has_permission(self, request, view):
        #   si es un get vas poder pasar o sea solo ver
          if request.method=='GET':
               return True
          else:
               return request.user.is_staff
               
          
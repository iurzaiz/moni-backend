from rest_framework.permissions import BasePermission


class IsPostOrIsAuthenticated(BasePermission):
     def has_permission(self, request, view):
         if request.method == 'POST' or request.method == 'GET' or request.method == 'PUT' or request.method == 'DELETE':        #eliminar la parte del get y put y delete
             return True
         return request.user and request.user.is_authenticated
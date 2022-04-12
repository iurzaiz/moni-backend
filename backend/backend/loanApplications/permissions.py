from rest_framework.permissions import BasePermission


class IsPostOrIsAuthenticated(BasePermission):
    #Autorizo solo a post sin estar logueado
     def has_permission(self, request, view):        
        if request.method == 'POST':  
             return True
        return request.user and request.user.is_authenticated
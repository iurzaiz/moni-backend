from django.urls import path, include
from backend.userAuthentication import views

urlpatterns = [
    path('', views.LoginApiView.as_view())
]
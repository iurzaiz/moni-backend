from django.urls import path
from . import views



urlpatterns = [
    path('applications/', views.LoanApplicationApiView.as_view()),
    path('applications/<pk>', views.ApplicationDetailApiView.as_view()),
]
 
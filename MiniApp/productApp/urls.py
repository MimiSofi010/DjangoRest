from django.urls import path
from productApp import views

urlpatterns = [
    path('electronics/', views.electronics),
    path('toys/', views.toys),
    path('shoes/', views.shoes),
]

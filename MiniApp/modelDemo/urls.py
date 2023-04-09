from django.urls import path
from modelDemo import views

urlpatterns = [
    path('employees/', views.employeeData),

]

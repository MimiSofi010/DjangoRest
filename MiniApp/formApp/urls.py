from django.urls import path
from formApp import views

urlpatterns = [
    path('user_registration/', views.userRegistrationView),

]

from django.urls import path
from firstapp import views

urlpatterns = [

    path('', views.display),
    path('datetime/', views.displayDateTime),

]

from django.urls import path
from login import views

urlpatterns = [
     path('', views.Home, name='Home'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Loginn, name='login')
]
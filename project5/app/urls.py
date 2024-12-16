from django.urls import path
from .import views

urlpattern=[
    path('',views.register),
    path('login',views.login),
    path('homepage',views.home),
    path('logout',views.logout),
    path('adminhomepage',views.adminhome),
    path('adminlogin',views.adminlogin),
]
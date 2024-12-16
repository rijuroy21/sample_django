from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('login',views.login),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('home',views.home),
]
from django.urls import path
from . import views

urlpatterns=[
    path('',views.register),
    path('login',views.login),
    path('homepage',views.home),
    path('logout',views.logout),
    path('adminhomepage',views.adminhome),
    path('adminlogin',views.adminlogin),
    path('update',views.update),
    path('user_stud',views.user_form_dis),
]
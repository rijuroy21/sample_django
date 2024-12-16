from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('register',views.register),
    path('homepage',views.home),
    path('logout',views.logout),
]

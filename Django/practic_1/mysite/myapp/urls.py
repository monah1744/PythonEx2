from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('user', views.user, name='user'),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),

]

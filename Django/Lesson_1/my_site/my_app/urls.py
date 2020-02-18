from django.urls import path

from my_site.my_app import views

urlpatterns = [
    path('', views.first, name='index'),
    path('hello', views.hello)
]

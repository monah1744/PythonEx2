from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.hello, name='hello'),
    path('article/', views.main_article, name='main_article'),
    path('article/archive/', views.article_archive, name='article_archive'),
    path('article/<int:article_number>/archive/',
         views.archive_number, name='archive_number'),
    path('article/33/', views.uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('article/<int:article_id>/<slug:name>',
         views.article, name='article_name'),
    path('users/', views.main_users, name='main_user'),
    path('users/<int:user_number>/', views.users_number, name='user_number'),
]

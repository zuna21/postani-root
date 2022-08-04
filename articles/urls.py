from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('article/<str:pk>/', views.article, name='article'),


    path('categories/', views.categories, name='categories'),
    path('category/<str:pk>/', views.category, name='category'),

    path('about', views.about, name='about'),

    path('create-article/', views.createArticle, name='create-article'),
]
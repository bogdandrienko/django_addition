from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index),
    path("index/", views.index),
    path("home/", views.index),
    #
    path("sales/", views.sales, name="sales"),
    #
    path("news/", views.news, name="news"),
    #
    path("ideas_list/", views.ideas_list, name="ideas_list"),
    path("ideas_create/", views.index, name="ideas_create"),
    path("ideas_rating/", views.index, name="ideas_rating"),
    #
    path("calculator/", views.calculator, name="calculator"),
]

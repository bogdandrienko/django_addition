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
]

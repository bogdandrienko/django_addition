from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    #
    path("sales/", views.sales, name="sales"),
]

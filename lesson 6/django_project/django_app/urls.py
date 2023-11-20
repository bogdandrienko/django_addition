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
    path("calculator/", views.calculator, name="calculator"),
    path("calculator2/", views.calculator2, name="calculator2"),
    #
    path("ideas_list/", views.ideas_list, name="ideas_list"),
    path("ideas_detail/<str:idea_id>/", views.ideas_detail, name="ideas_detail"),
    path("ideas_create/", views.ideas_create, name="ideas_create"),
    path("ideas_update/<str:idea_id>/", views.ideas_update, name="ideas_update"),
    path("ideas_delete/<str:idea_id>/", views.ideas_delete, name="ideas_delete"),
]

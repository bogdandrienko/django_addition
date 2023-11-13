from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),  # admin site
    #
    path("", include("django_app.urls")),
    # path("", include("django_payments.urls")),
]

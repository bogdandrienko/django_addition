from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "price",
        "phone",
        "is_active",
        "date_time",
    )
    list_display_links = (
        "title",
        "phone",
    )
    list_editable = ("is_active",)
    list_filter = (
        "title",
        "description",
        "price",
        "phone",
        "is_active",
        "date_time",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "title",
                    "description",
                    "price",
                    "phone",
                )
            },
        ),
        (
            "Дополнительные данные",
            {
                "fields": (
                    "is_active",
                    "date_time",
                )
            },
        ),
    )
    search_fields = [
        "title",
        "description",
        "phone",
    ]


# admin.site.register(models.Service)  # simple registration
admin.site.register(models.Service, ServiceModelAdmin)  # complex registration

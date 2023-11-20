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


class IdeaModelAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "description",
        "budget",
        "avatar",
        "additional",
        "is_active",
        "date_time",
    )
    list_display_links = (
        "author",
        "title",
    )
    list_editable = ("is_active", "budget")
    list_filter = (
        "author",
        "title",
        "description",
        "budget",
        "avatar",
        "additional",
        "is_active",
        "date_time",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "author",
                    "title",
                    "description",
                    "budget",
                    "avatar",
                    "additional",
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
        "budget",
    ]

class PriceModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
    )
    list_display_links = (
        "title",
    )
    list_editable = ("price",)
    list_filter = (
        "title",
        "price",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "title",
                )
            },
        ),
        (
            "Дополнительные данные",
            {
                "fields": (
                    "price",
                )
            },
        ),
    )
    search_fields = [
        "title",
        "price",
    ]

# admin.site.register(models.Service)  # simple registration
admin.site.register(models.Service, ServiceModelAdmin)  # complex registration
admin.site.register(models.Idea, IdeaModelAdmin)  # complex registration
admin.site.register(models.Price, PriceModelAdmin)

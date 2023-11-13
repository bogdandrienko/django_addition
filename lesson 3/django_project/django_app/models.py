from django.db import models
from django.utils.timezone import now

"""
Тут происходит "описание"(настройка) базы данных

class Service(models.Model):  # таблица
    title = models.CharField( # колонка
    max_length=300 # параметры колонки(столбец)
    )  
"""


class Service(models.Model):  # таблица в базе данных
    # boolean = models.BooleanField(
    #     db_column='boolean_db_column',
    #     db_index=True,
    #     db_tablespace='boolean_db_tablespace',
    #     primary_key=False,
    #     # choices=LIST_DB_VIEW_CHOICES,
    #     unique=False,
    #     editable=True,
    #     blank=True,
    #     null=False,
    #     default=False,
    #     verbose_name='boolean',
    #     help_text='<small class="text-muted">BooleanField</small><hr><br>',
    # )

    # id = serial
    # наименование, описание, цену, номер телефона, время создания
    title = models.CharField(
        verbose_name='наименование',
        max_length=300  # текст длиной <= 300
    )
    description = models.TextField(verbose_name='описание')  # текст
    price = models.IntegerField(verbose_name='цена')  # число
    phone = models.TextField(verbose_name='номер телефона')  # текст
    is_active = models.BooleanField(verbose_name='активность объявления', default=True)  # булево
    date_time = models.DateTimeField(verbose_name='время создания', default=now)  # дата и время

    class Meta:
        app_label = 'django_app'
        ordering = ('-is_active', '-date_time')
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f"{self.title}"

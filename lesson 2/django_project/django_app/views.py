from django.http import HttpResponse
from django.shortcuts import render
from django_app import models


def index(request):  # view (controller) - бизнес логика
    return HttpResponse("hello world")


def sales(request):
    # sales_list = []
    # for i in range(1, 20 + 1):
    #     sales_list.append(
    #         {
    #             "id": i,
    #             "title": f"Продам верблюда {i}",
    #             "description": "Продам верблюда Продам верблюда Продам верблюда",
    #             "phone": "+7 771 293 12 37",
    #             "price": 6200.5 * i,
    #             "count": 10 / i,
    #         }
    #     )
    #
    # sale = {
    #     "id": 1,
    #     "title": "Продам верблюда",
    #     "description": "Продам верблюда Продам верблюда Продам верблюда",
    #     "phone": "+7 771 293 12 37",
    #     "price": 6200.5,
    #     "count": 10,
    # }
    #
    # a = 12
    # b = 13
    # if a > b:
    #     print("Больше")
    # else:
    #     print("Меньше")
    name = "Marina"
    status = False
    numbers = [1, 2, 3, 4, 5]
    # services = models.Service.objects.all()  # all - все, get(id=1) - один,
    services = models.Service.objects.all().filter(is_active=True)  # filter - фильтрация
    context = {"services": services, "name": name, "status": status, "numbers": numbers}
    return render(request, "sales.html", context=context)

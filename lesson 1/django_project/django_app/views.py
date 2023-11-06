from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # view (controller) - бизнес логика
    return HttpResponse("hello world")


def sales(request):
    sales_list = []
    for i in range(1, 20 + 1):
        sales_list.append(
            {
                "id": i,
                "title": f"Продам верблюда {i}",
                "description": "Продам верблюда Продам верблюда Продам верблюда",
                "phone": "+7 771 293 12 37",
                "price": 6200.5 * i,
                "count": 10 / i,
            }
        )

    sale = {
        "id": 1,
        "title": "Продам верблюда",
        "description": "Продам верблюда Продам верблюда Продам верблюда",
        "phone": "+7 771 293 12 37",
        "price": 6200.5,
        "count": 10,
    }

    context = {"sale": sale, "sales_list": sales_list}

    a = 12
    b = 13
    if a > b:
        print("Больше")
    else:
        print("Меньше")

    return render(request, "sales.html", context=context)

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models


def index(request):  # view (controller) - бизнес логика
    # return HttpResponse("hello world")
    return render(request, "home.html", context={})

# Bogdan123
# 6-$ej@cC8*tffCe


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
    # services.order_by("name", "") # - сортировка
    context = {"services": services, "name": name, "status": status, "numbers": numbers}
    return render(request, "sales.html", context=context)


def news(request):
    return render(request, "news.html", context={})


def ideas_list(request):
    # выборка из базы данных ВСЕХ ".all()" идей, затем их фильтрация только по активным ".filter(is_active=True)"
    ideas_objs = models.Idea.objects.all().filter(is_active=True)
    # создание переменной которая будет "контейнером" для передаваемых данных
    context = {"ideas_list": ideas_objs}
    # передача(проброс) данных в html страницу(шаблон)
    return render(request, "IdeasList.html", context=context)


def ideas_detail(request, idea_id):
    # выборка из базы данных одной идеи по её "idea_id"
    ideas_obj = models.Idea.objects.get(id=int(idea_id))
    # создание переменной которая будет "контейнером" для передаваемых данных
    context = {"idea": ideas_obj}
    # передача(проброс) данных в html страницу(шаблон)
    return render(request, "IdeasDetail.html", context=context)


def ideas_delete(request, idea_id):
    # выборка из базы данных одной идеи по её "idea_id"
    ideas_obj = models.Idea.objects.get(id=int(idea_id))

    # удаление
    # ideas_obj.delete()

    # изменение видимости(статуса)
    ideas_obj.is_active = False
    ideas_obj.save()

    # перенаправление на страницу со всеми идеями
    return redirect(reverse('ideas_list'))


def ideas_create(request):
    if request.method == 'GET':
        context = {"message": None}
        return render(request, "IdeasCreate.html", context=context)
    if request.method == 'POST':
        print(request.POST)  # обычные данные
        print(request.FILES)  # файлы

        title = str(request.POST.get('title'))
        description = str(request.POST.get('description'))
        budget = int(request.POST.get('budget'))
        avatar = request.FILES.get('avatar')
        additional = request.FILES.get('additional')

        models.Idea.objects.create(
            author=request.user.username,
            title=title,
            description=description,
            budget=budget,
            avatar=avatar,
            additional=additional
        )
        context = {"message": "Идея успешно подана!"}
        return render(request, "IdeasCreate.html", context=context)


def ideas_update(request, idea_id):
    if request.method == 'GET':
        ideas_obj = models.Idea.objects.get(id=int(idea_id))
        context = {"idea": ideas_obj}
        return render(request, "IdeasUpdate.html", context=context)
    if request.method == 'POST':
        print(request.POST)  # обычные данные
        print(request.FILES)  # файлы

        title = str(request.POST.get('title'))
        description = str(request.POST.get('description'))
        budget = int(request.POST.get('budget'))
        avatar = request.FILES.get('avatar')
        additional = request.FILES.get('additional')

        ideas_obj = models.Idea.objects.get(id=int(idea_id))
        ideas_obj.author = request.user.username
        ideas_obj.title = title
        ideas_obj.description = description
        ideas_obj.budget = budget
        if avatar:
            ideas_obj.avatar = avatar
        if additional:
            ideas_obj.additional = additional
        ideas_obj.save()

        return redirect(reverse('ideas_list'))


def calculator(request):
    itog_val = 0
    if request.method == "POST":
        print(request.POST)
        """
<QueryDict: 'credit': ['ИП'], 'nalog': ['Упрощённый'], 'type': ['Услуги'], 'CountPep': ['3'], 'CountDoc': ['0']}>
        """
        credit = str(request.POST.get('credit'))
        nalog = str(request.POST.get('nalog'))
        type = str(request.POST.get('type'))
        CountPep = str(request.POST.get('CountPep'))
        CountDoc = str(request.POST.get('CountDoc'))
        print(credit, nalog, type, CountPep, CountDoc)

        default_val = models.Price.objects.get(title="Стандартное значение").price
        itog_val = default_val
        if credit == "ТОО":
            itog_val += models.Price.objects.get(title="Сумма ТОО").price

        if type == "Торговля" and (nalog == "Упрощённый" or nalog == "Розничный"):
            itog_val += 20000

        if CountPep == "1":
            itog_val += models.Price.objects.get(title="Уровень 1 людей").price
        if CountPep == "2":
            itog_val += models.Price.objects.get(title="Уровень 2 людей").price
        if CountPep == "3":
            itog_val += 30000
        if CountPep == "4":
            itog_val += 40000

    context = {"itog_val": itog_val}
    return render(request, "calculator.html", context=context)


def calculator2(request):
    return render(request, "calculator2.html", context={})

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Company
#
# def index(request):
#     return HttpResponse("<h1>Компания</h1>")

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Company


# получение данных из бд
def index(request):
    people = Company.objects.all()
    return render(request, "test.html", {"people": people})

# # сохранение данных в бд
# # def create(request):
# #     if request.method == "POST":
# #         tom = Company()
# #         tom.name = request.POST.get("name")
# #         tom.age = request.POST.get("age")
# #         tom.save()
# #     return HttpResponseRedirect("/")
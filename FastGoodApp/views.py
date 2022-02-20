from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def food_home(request):
    shaurma = Shaurma_Food.objects.all()
    return render(request,'FastGoodApp/home_page.html', {'title':'Главная страница','shaurma_menu':shaurma})


def food_menu(request):
    return HttpResponse('Меню')

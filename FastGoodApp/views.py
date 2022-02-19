from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def food_home(request):
    return render(request,'FastGoodApp/home_page.html')


def food_menu(request):
    return HttpResponse('Меню')

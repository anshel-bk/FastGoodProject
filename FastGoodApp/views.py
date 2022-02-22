from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import *
# Create your views here.


def food_home(request):
    shaurma = Shaurma_Food.objects.all()
    return render(request,'FastGoodApp/home_page.html', {'title':'Главная страница','shaurma_menu':shaurma})


def product_info(request,shaurma_slug):
    shaurma = Shaurma_Food.objects.filter(slug=shaurma_slug)
    post = get_object_or_404(Shaurma_Food, slug=shaurma_slug)
    return render(request,'FastGoodApp/product_info.html',{'shaurma_menu':shaurma})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'FastGoodApp/register.html'
    success_url = reverse_lazy('login')


def login(request):
    return HttpResponse('Успешная регистрация')
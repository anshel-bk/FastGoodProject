from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView

from .forms import RegisterUserForm, LoginUserForm, ContactForm
from .models import *
from .utils import *
# Create your views here.


class FoodHome(DataMixin,ListView):
    model = Shaurma_Food

    template_name = 'FastGoodApp/home_page.html'
    context_object_name = 'shaurma_menu'

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Главная страница")
            context = dict(list(context.items()) + list(c_def.items()))
            return context

class ProductInfo(DataMixin,ListView):
    model = Shaurma_Food
    template_name = 'FastGoodApp/product_info.html'
    context_object_name = 'shaurma_menu'
    slug_url_kwarg = 'shaurma_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Информация о продукте'
        return context

    def get_queryset(self):
        return Shaurma_Food.objects.filter(slug=self.kwargs['shaurma_slug'])

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'FastGoodApp/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'FastGoodApp/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id} корректное")


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'FastGoodApp/feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
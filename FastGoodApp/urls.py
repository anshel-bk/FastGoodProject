from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login

from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('home/', FoodHome.as_view(), name='home'),
    path('product/<slug:shaurma_slug>/', ProductInfo.as_view(), name='product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

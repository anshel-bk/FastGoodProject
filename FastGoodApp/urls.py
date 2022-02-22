from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login

from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('home/', food_home, name='home'),
    path('product/<slug:shaurma_slug>/', product_info, name='product'),
    path('register',RegisterUser.as_view(),name='register'),
    path('login',LoginUser.as_view(),name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
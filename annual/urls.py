from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('data/', ResponseApi.as_view(), name='data'),
]
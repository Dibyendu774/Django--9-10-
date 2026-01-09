from .views import *
from django.urls import path

urlpatterns = [
    path('', Home),
    path('Register-Page', Register)
]
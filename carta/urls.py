
from django.urls import path
from . import views

urlpatterns = [
    path('', views.carta, name='carta_list'),
]
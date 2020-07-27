from django.urls import path
from . import views

urlpatterns = [
    path('', views.carta_list, name='carta_list'),
]
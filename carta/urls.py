from django.urls import path
from . import views

urlpatterns = [
    path('', views.carta_list, name='carta_list'),
    path('index', views.carta_list, name='carta_list'),
    path('about', views.about, name='about'),
    path('carta', views.carta, name='carta'),
    path('contact', views.contact, name='contacto'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('lista_convidados', views.lista_convidados, name = "lista_convidados")
]
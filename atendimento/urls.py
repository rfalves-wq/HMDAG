from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_atendimento, name='novo_atendimento'),
    path('lista/', views.lista_atendimentos, name='lista_atendimentos'),
]

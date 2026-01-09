from django.urls import path
from . import views
from django.urls import path
from .views import criar_atendimento
urlpatterns = [
    path('novo/', views.criar_atendimento, name='novo_atendimento'),
   # path('lista/', views.lista_atendimentos, name='lista_atendimentos'),
    path('novo/<int:paciente_id>/', criar_atendimento, name='novo_atendimento'),
]

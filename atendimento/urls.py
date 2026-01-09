from django.urls import path
from .views import criar_atendimento, fila_medica

urlpatterns = [
    path('novo/', criar_atendimento, name='novo_atendimento'),
    path('fila/', fila_medica, name='fila_medica'),
]

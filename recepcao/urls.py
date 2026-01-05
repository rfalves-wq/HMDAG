from django.urls import path
from .views import atendimento_create, fila_triagem

urlpatterns = [
    path('recepcao/novo/', atendimento_create, name='atendimento_create'),
    path('recepcao/fila/', fila_triagem, name='fila_triagem'),
]

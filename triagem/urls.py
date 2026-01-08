from django.urls import path
from . import views

urlpatterns = [
    path('triagem/', views.fila_triagem, name='fila_triagem'),
    path('triagem/iniciar/<int:atendimento_id>/', views.iniciar_triagem, name='iniciar_triagem'),
    path('triagem/concluir/<int:atendimento_id>/', views.concluir_triagem, name='concluir_triagem'),
]

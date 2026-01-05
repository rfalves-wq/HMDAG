from django.urls import path
from .views import atendimento_create, fila_triagem
from . import views
urlpatterns = [
   # path('recepcao/novo/', atendimento_create, name='atendimento_create'),
    path('recepcao/fila/', fila_triagem, name='fila_triagem'),
    path('recepcao/novo/', atendimento_create, name='atendimento_novo'),
    path('recepcao/novo/<int:paciente_id>/', atendimento_create, name='atendimento_create'),
path('atendimento/novo/', views.atendimento_create, name='atendimento_create')

]

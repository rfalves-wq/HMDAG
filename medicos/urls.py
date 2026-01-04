from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/novo/', views.medico_create, name='medico_create'),
    path('medicos/<int:pk>/editar/', views.medico_update, name='medico_update'),
    path('medicos/<int:pk>/excluir/', views.medico_delete, name='medico_delete'),
]

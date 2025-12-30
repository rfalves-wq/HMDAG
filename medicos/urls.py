from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('', views.medico_list, name='lista'),
    path('novo/', views.medico_create, name='criar'),
    path('<int:pk>/editar/', views.medico_update, name='editar'),
    path('<int:pk>/excluir/', views.medico_delete, name='excluir'),
]

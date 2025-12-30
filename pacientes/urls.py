from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
     path('list/', views.PacienteListView.as_view(), name='list'),
     path('create/', views.PacienteCreateView.as_view(), name='create'),
  
]

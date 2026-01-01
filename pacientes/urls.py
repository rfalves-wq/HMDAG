from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
     path('pacientes/list/', views.PacienteListView.as_view(), name='list'),
     path('pacientes/create/', views.PacienteCreateView.as_view(), name='create'),
     path('pacientes/<int:pk>/detail/', views.PacienteDetailView.as_view(), name='detail'),
     path('pacientes/<int:pk>/update/', views.PacienteUpdateView.as_view(), name='update'),
     path('pacientes/<int:pk>/delete/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
]

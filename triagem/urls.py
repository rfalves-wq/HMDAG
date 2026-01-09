from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redireciona /triagem/ para /triagem/fila/
    path('', RedirectView.as_view(pattern_name='fila_triagem', permanent=False)),
    
    path('fila/', views.fila_triagem, name='fila_triagem'),
    path('atender/<int:triagem_id>/', views.triagem_atender, name='triagem_atender'),
    
]

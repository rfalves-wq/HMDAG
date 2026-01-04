from django.urls import path
from .views import (
    TecnicoEnfermagemListView,
    TecnicoEnfermagemCreateView,
    TecnicoEnfermagemUpdateView,
    TecnicoEnfermagemDetailView,
    TecnicoEnfermagemDeleteView,
)

urlpatterns = [
    path('', TecnicoEnfermagemListView.as_view(), name='tecnico_enfermagem_list'),
    path('novo/', TecnicoEnfermagemCreateView.as_view(), name='tecnico_enfermagem_create'),
    path('<int:pk>/editar/', TecnicoEnfermagemUpdateView.as_view(), name='tecnico_enfermagem_update'),
    path('<int:pk>/', TecnicoEnfermagemDetailView.as_view(), name='tecnico_enfermagem_detail'),
    path('<int:pk>/excluir/', TecnicoEnfermagemDeleteView.as_view(), name='tecnico_enfermagem_delete'),
]

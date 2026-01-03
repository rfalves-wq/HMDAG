from django.urls import path
from .views import (
    EnfermeiroListView,
    EnfermeiroCreateView,
    EnfermeiroUpdateView,
    EnfermeiroDetailView,
    enfermeiro_desativar
)

urlpatterns = [
    path('enfermeiros/', EnfermeiroListView.as_view(), name='enfermeiro_list'),
    path('enfermeiros/novo/', EnfermeiroCreateView.as_view(), name='enfermeiro_create'),
    path('enfermeiros/<int:pk>/editar/', EnfermeiroUpdateView.as_view(), name='enfermeiro_update'),
    path('enfermeiros/<int:pk>/', EnfermeiroDetailView.as_view(), name='enfermeiro_detail'),
    path('enfermeiros/<int:pk>/desativar/', enfermeiro_desativar, name='enfermeiro_desativar'),
]

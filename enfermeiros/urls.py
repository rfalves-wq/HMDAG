from django.urls import path
from . import views

app_name = 'enfermeiros'

urlpatterns = [
     path('list/', views.EnfermeiroListView.as_view(), name='list'),
     path('create/', views.EnfermeiroCreateView.as_view(), name='create'),
     path('<int:pk>/detail/', views.EnfermeiroDetailView.as_view(), name='detail'),
      path('<int:pk>/update/', views.EnfermeiroUpdateView.as_view(), name='update'),
]

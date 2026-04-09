from django.urls import path
from .views import EncuentroListView, EncuentroDetailView

urlpatterns = [
    # Lista + filtros (query params) + creación
    path('', EncuentroListView.as_view(), name='encuentro-list'),

    # Detalle, actualización y eliminación por pk
    path('<int:pk>/', EncuentroDetailView.as_view(), name='encuentro-detail'),
]

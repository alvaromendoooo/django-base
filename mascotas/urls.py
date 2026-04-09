from django.urls import path
from .views import (
    TipoMascotaListView,
    TipoMascotaDetailView,
    MascotaListView,
    MascotaDetailView,
)

urlpatterns = [
    # Tipos de mascota
    path('tipos/', TipoMascotaListView.as_view(), name='tipo-mascota-list'),
    path('tipos/<int:pk>/', TipoMascotaDetailView.as_view(), name='tipo-mascota-detail'),

    # Mascotas
    path('', MascotaListView.as_view(), name='mascota-list'),
    path('<int:pk>/', MascotaDetailView.as_view(), name='mascota-detail'),
]

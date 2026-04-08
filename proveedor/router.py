from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(prefix="proveedor", basename = "proveedor", viewset = ProveedorView)
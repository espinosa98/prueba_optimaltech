from rest_framework import routers
from app.api import views

router = routers.DefaultRouter()

router.register('productos/listar', views.ProductoListView, basename='listar_poductos')
router.register('productos/crear', views.ProductoCreateUpdateView, basename='crear_producto')
router.register('productos/eliminar', views.ProductoDeleteView, basename='eliminar_producto')

from django.urls import path
from app.views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='listar_productos'),
    path('crear-producto/', ProductoCreateView.as_view(), name='crear_producto'),
    path('editar-producto/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar-producto/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto'),

]
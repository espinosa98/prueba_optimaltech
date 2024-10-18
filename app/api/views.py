from django.shortcuts import get_object_or_404
# Django
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

# Propios
from app.api.serializer import ProductoSerializer
from app.models import Producto


class ProductoListView(ReadOnlyModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            data = self.serializer_class(queryset, many=True).data

            if data:
                return Response({'status': status.HTTP_200_OK,
                                 'message':'La consulta fue exitosa', 'data':data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': status.HTTP_202_ACCEPTED,
                                 'message':'No se encontro los Productos', 'data':[]}, status=status.HTTP_202_ACCEPTED)

        except Exception as exc:
            return Response({'status':status.HTTP_400_BAD_REQUEST,
                             'message':'La consulta falló, por favor validar', 'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)


class ProductoCreateUpdateView(ReadOnlyModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


    def create(self, request, *args, **kwargs):
        try:
            id_producto = request.data.get('id_producto', None)
            if not id_producto:
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                                 'message': 'El id_producto es requerido', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
            try:
                producto = Producto.objects.get(id=id_producto)
            except Producto.DoesNotExist:
                producto = None

            data = request.data
            serializer = self.serializer_class(producto, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                {'status': status.HTTP_200_OK if producto else status.HTTP_201_CREATED,
                 'message': 'El producto fue actualizado exitosamente' if producto else 'El producto fue creado exitosamente',
                 'data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as exc:
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST, 'message': 'La consulta falló, por favor validar',
                 'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)


class ProductoDeleteView(ReadOnlyModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            id_producto = request.data.get('id_producto', None)
            if not id_producto:
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                                 'message': 'El id_producto es requerido', 'data': []}, status=status.HTTP_400_BAD_REQUEST)

            try:
                producto = Producto.objects.get(id=id_producto)
            except Producto.DoesNotExist:
                producto = None

            if producto:
                producto.delete()
                return Response({'status': status.HTTP_200_OK,
                                 'message': 'El producto fue eliminado exitosamente', 'data': []}, status=status.HTTP_200_OK)
            else:
                return Response({'status': status.HTTP_202_ACCEPTED,
                                 'message': 'El producto no existe', 'data': []}, status=status.HTTP_202_ACCEPTED)

        except Exception as exc:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'La consulta falló, por favor validar', 'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
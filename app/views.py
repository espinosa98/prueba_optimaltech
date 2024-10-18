# Standard Library

# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect
from django.contrib import messages

# Propio
from app.models import Producto
from app.forms import ProductoForm


class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

    def get_queryset(self):
        return Producto.objects.all()


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('listar_productos')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Producto creado con éxito')
        return super().form_valid(form)


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('listar_productos')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Producto actualizado con éxito')
        return super().form_valid(form)


class ProductoDeleteView(View):

    def get(self, request, *args, **kwargs):
        producto = Producto.objects.get(id=self.kwargs['pk'])
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito')
        return HttpResponseRedirect(reverse_lazy('listar_productos'))


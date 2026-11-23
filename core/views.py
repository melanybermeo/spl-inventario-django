from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import ProductoForm
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = "core/producto_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        qs = super().get_queryset().select_related("categoria")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(nombre__icontains=q) | Q(codigo__icontains=q))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        # Bandera de configuración usada en la vista (Sesión 2):
        # solo si la variante incluye reportes se ofrece exportar.
        if settings.ENABLE_REPORTS:
            context["formatos_exportacion"] = settings.REPORT_FORMATS
        else:
            context["formatos_exportacion"] = []
        return context


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "core/producto_form.html"
    success_url = reverse_lazy("core:producto_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto registrado correctamente.")
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "core/producto_form.html"
    success_url = reverse_lazy("core:producto_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)

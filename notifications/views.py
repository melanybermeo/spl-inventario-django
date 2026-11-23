from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import Notificacion


class NotificacionListView(ListView):
    model = Notificacion
    template_name = "notifications/notificacion_list.html"
    context_object_name = "notificaciones"

    def get_queryset(self):
        return super().get_queryset().select_related("producto")


@require_POST
def marcar_leida(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    notificacion.leida = True
    notificacion.save(update_fields=["leida"])
    return redirect("notifications:lista")

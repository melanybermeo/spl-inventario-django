from .models import Notificacion


def unread_notifications(request):
    return {"notificaciones_pendientes": Notificacion.objects.filter(leida=False).count()}

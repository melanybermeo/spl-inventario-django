from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Producto

from .models import Notificacion


@receiver(post_save, sender=Producto)
def alerta_stock_bajo(sender, instance, **kwargs):
    """Crea (o actualiza) una alerta cuando el stock baja del mínimo."""
    if instance.bajo_stock:
        Notificacion.objects.update_or_create(
            producto=instance,
            leida=False,
            defaults={
                "mensaje": (
                    f"Stock bajo: {instance.nombre} tiene {instance.stock} "
                    f"unidades (mínimo {instance.stock_minimo})."
                )
            },
        )

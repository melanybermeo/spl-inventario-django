from django.db import models


class Notificacion(models.Model):
    producto = models.ForeignKey(
        "core.Producto", on_delete=models.CASCADE, related_name="notificaciones"
    )
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["leida", "-creada"]
        verbose_name = "notificación"
        verbose_name_plural = "notificaciones"

    def __str__(self):
        return self.mensaje

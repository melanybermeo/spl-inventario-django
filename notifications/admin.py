from django.contrib import admin

from .models import Notificacion


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ["mensaje", "producto", "leida", "creada"]
    list_filter = ["leida"]

from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"
    verbose_name = "Notificaciones (funcionalidad opcional)"

    def ready(self):
        # Conecta las señales solo cuando la app está instalada.
        from . import signals  # noqa: F401

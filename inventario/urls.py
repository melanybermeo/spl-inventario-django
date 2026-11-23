"""
Rutas del proyecto.

Las rutas del núcleo siempre se registran. Las rutas de las apps
opcionales se agregan con include() condicional según las banderas
generadas a partir de config_product.py.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cuentas/", include("accounts.urls")),
    path("", include("core.urls")),
]

# include() condicional: en la Variante A estas rutas no existen (404).
if settings.ENABLE_REPORTS:
    urlpatterns.append(path("reportes/", include("reports.urls")))

if settings.ENABLE_NOTIFICATIONS:
    urlpatterns.append(path("notificaciones/", include("notifications.urls")))

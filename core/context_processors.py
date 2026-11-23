from django.conf import settings


def product_features(request):
    """Pone a disposición de todas las plantillas la variante y sus características."""
    return {
        "product": {
            "variant": settings.PRODUCT_VARIANT,
            "name": settings.PRODUCT_NAME,
        },
        "features": {
            "reports": settings.ENABLE_REPORTS,
            "notifications": settings.ENABLE_NOTIFICATIONS,
            "report_formats": settings.REPORT_FORMATS,
        },
    }

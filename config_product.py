"""
config_product.py
-----------------
Definición de las variantes de la línea de productos "Inventario SPL".

Cada variante es un diccionario de características (features). settings.py
lee la variante activa y convierte estas características en banderas
(ENABLE_REPORTS, ENABLE_NOTIFICATIONS, ...) que usan urls.py, las vistas
y las plantillas.

Para elegir la variante se usa la variable de entorno PRODUCT_VARIANT:
    Windows (PowerShell):  $env:PRODUCT_VARIANT="A"
    Windows (cmd):         set PRODUCT_VARIANT=A
    Linux / macOS:         export PRODUCT_VARIANT=A
Si no se define, se usa DEFAULT_VARIANT.
"""
import os

# Variante A: sistema básico, sin funcionalidades extra.
PRODUCT_A = {
    "NAME": "Variante A - Inventario Básico",
    "ENABLE_REPORTS": False,
    "ENABLE_NOTIFICATIONS": False,
    "REPORT_FORMATS": [],
}

# Variante B: sistema completo, con funcionalidades extendidas.
PRODUCT_B = {
    "NAME": "Variante B - Inventario Completo",
    "ENABLE_REPORTS": True,
    "ENABLE_NOTIFICATIONS": True,
    "REPORT_FORMATS": ["pdf", "csv"],
}

PRODUCTS = {
    "A": PRODUCT_A,
    "B": PRODUCT_B,
}

DEFAULT_VARIANT = "B"
VALID_REPORT_FORMATS = {"pdf", "csv"}


def get_active_variant():
    """Devuelve la letra de la variante activa (A o B)."""
    return os.environ.get("PRODUCT_VARIANT", DEFAULT_VARIANT).strip().upper()


def validate(product):
    """Verifica las restricciones del modelo de características."""
    formats = set(product.get("REPORT_FORMATS", []))
    if formats and not product["ENABLE_REPORTS"]:
        raise ValueError("REPORT_FORMATS requiere ENABLE_REPORTS = True.")
    if product["ENABLE_REPORTS"] and not formats:
        raise ValueError("Si ENABLE_REPORTS = True se debe elegir al menos un formato.")
    invalid = formats - VALID_REPORT_FORMATS
    if invalid:
        raise ValueError(f"Formatos no soportados: {', '.join(sorted(invalid))}")
    return product


def get_product(variant=None):
    """Devuelve el diccionario de características de la variante pedida."""
    variant = (variant or get_active_variant()).upper()
    if variant not in PRODUCTS:
        raise ValueError(
            f"La variante '{variant}' no existe. Opciones: {', '.join(PRODUCTS)}"
        )
    return validate(PRODUCTS[variant])

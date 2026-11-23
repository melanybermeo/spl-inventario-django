"""
Configuración del proyecto "Inventario SPL".

La parte importante para la práctica está en la sección
"LÍNEA DE PRODUCTOS": aquí se lee config_product.py y se generan
las banderas que activan o desactivan cada funcionalidad opcional.
"""
from pathlib import Path

from config_product import get_active_variant, get_product

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# LÍNEA DE PRODUCTOS (gestión de la variabilidad)
# ---------------------------------------------------------------------------
PRODUCT_VARIANT = get_active_variant()
PRODUCT = get_product(PRODUCT_VARIANT)

PRODUCT_NAME = PRODUCT["NAME"]
ENABLE_REPORTS = PRODUCT["ENABLE_REPORTS"]
ENABLE_NOTIFICATIONS = PRODUCT["ENABLE_NOTIFICATIONS"]
REPORT_FORMATS = PRODUCT["REPORT_FORMATS"]

# ---------------------------------------------------------------------------
# Configuración general
# ---------------------------------------------------------------------------
SECRET_KEY = "django-insecure-solo-para-la-practica-gcs"
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Núcleo común: lo tienen TODAS las variantes.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",  # reutilizable: autenticación y registro
    "core",      # específico: gestión de productos
]

# Apps opcionales: solo se instalan si la variante las incluye.
if ENABLE_REPORTS:
    INSTALLED_APPS.append("reports")
if ENABLE_NOTIFICATIONS:
    INSTALLED_APPS.append("notifications")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "inventario.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Expone 'product' y 'features' a todas las plantillas.
                "core.context_processors.product_features",
            ],
        },
    },
]

if ENABLE_NOTIFICATIONS:
    TEMPLATES[0]["OPTIONS"]["context_processors"].append(
        "notifications.context_processors.unread_notifications"
    )

WSGI_APPLICATION = "inventario.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]

LANGUAGE_CODE = "es-ec"
TIME_ZONE = "America/Guayaquil"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "core:producto_list"
LOGOUT_REDIRECT_URL = "core:producto_list"

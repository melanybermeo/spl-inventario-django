# Inventario SPL – Línea de productos basada en Django

Práctica 4 – Gestión de la Configuración de Software (UNEMI).

Un mismo código base genera dos productos:

| Variante | Nombre | Reportes (PDF/CSV) | Notificaciones de stock |
|---|---|---|---|
| A | Inventario Básico | No | No |
| B | Inventario Completo | Sí | Sí |

## Estructura

```
spl_inventario/
├── config_product.py      # definición de las variantes A y B
├── manage.py
├── requirements.txt
├── inventario/            # proyecto: settings.py (banderas) y urls.py (include condicional)
├── templates/base.html    # menú con {% if features.* %}
├── accounts/              # REUTILIZABLE: ingreso, salida, registro
├── core/                  # NÚCLEO / ESPECÍFICO: productos y categorías
├── reports/               # OPCIONAL: panel, exportar PDF y CSV
└── notifications/         # OPCIONAL: alertas de stock bajo (señal post_save)
```

## Instalación (una sola vez)

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate        # con la variante B (por defecto) se crean todas las tablas
python manage.py cargar_demo    # productos de ejemplo + usuario admin / admin12345
```

## Ejecutar cada variante

PowerShell:
```powershell
$env:PRODUCT_VARIANT="A"; python manage.py runserver
$env:PRODUCT_VARIANT="B"; python manage.py runserver
```

CMD:
```cmd
set PRODUCT_VARIANT=A && python manage.py runserver
```

Linux / macOS:
```bash
PRODUCT_VARIANT=A python manage.py runserver
```

Abrir http://127.0.0.1:8000/ y comparar. En la variante A no aparecen
"Reportes", "Alertas" ni los botones de exportar, y `/reportes/` devuelve 404.

## Crear una variante nueva

En `config_product.py`:

```python
PRODUCT_C = {
    "NAME": "Variante C - Inventario con reportes",
    "ENABLE_REPORTS": True,
    "ENABLE_NOTIFICATIONS": False,
    "REPORT_FORMATS": ["csv"],
}
PRODUCTS = {"A": PRODUCT_A, "B": PRODUCT_B, "C": PRODUCT_C}
```

Luego `PRODUCT_VARIANT=C python manage.py runserver`.

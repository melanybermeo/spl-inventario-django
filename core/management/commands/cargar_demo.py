from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.models import Categoria, Producto

DATOS = [
    ("LAP-001", "Laptop Lenovo IdeaPad 3", "Computación", "689.90", 12, 5),
    ("MON-002", "Monitor Samsung 24\"", "Computación", "159.00", 3, 5),
    ("TEC-003", "Teclado mecánico Redragon", "Accesorios", "45.50", 25, 10),
    ("MOU-004", "Mouse inalámbrico Logitech", "Accesorios", "18.75", 4, 10),
    ("IMP-005", "Impresora Epson L3250", "Impresión", "229.00", 7, 3),
    ("TIN-006", "Tinta Epson 544 negra", "Impresión", "12.40", 2, 15),
    ("ROU-007", "Router TP-Link Archer C6", "Redes", "54.99", 9, 4),
    ("SWI-008", "Switch 8 puertos D-Link", "Redes", "27.30", 15, 5),
]


class Command(BaseCommand):
    help = "Carga productos de ejemplo y crea el usuario admin/admin12345."

    def handle(self, *args, **options):
        for codigo, nombre, cat, precio, stock, minimo in DATOS:
            categoria, _ = Categoria.objects.get_or_create(nombre=cat)
            Producto.objects.update_or_create(
                codigo=codigo,
                defaults={
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": Decimal(precio),
                    "stock": stock,
                    "stock_minimo": minimo,
                },
            )
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin12345")
        self.stdout.write(self.style.SUCCESS(f"{len(DATOS)} productos cargados."))

"""
App opcional de reportes.

Solo se instala cuando ENABLE_REPORTS = True. Cada formato de exportación
(PDF, CSV) es una sub-característica que se habilita en REPORT_FORMATS.
"""
import csv
from io import BytesIO

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from core.models import Producto


def _verificar_formato(formato):
    if formato not in settings.REPORT_FORMATS:
        raise Http404(f"El formato {formato.upper()} no está habilitado en esta variante.")


def panel(request):
    productos = list(Producto.objects.select_related("categoria"))
    por_categoria = {}
    for p in productos:
        fila = por_categoria.setdefault(p.categoria.nombre, {"cantidad": 0, "valor": 0})
        fila["cantidad"] += 1
        fila["valor"] += p.valor_total
    contexto = {
        "total_productos": len(productos),
        "total_unidades": sum(p.stock for p in productos),
        "valor_inventario": sum(p.valor_total for p in productos),
        "bajo_stock": [p for p in productos if p.bajo_stock],
        "por_categoria": sorted(por_categoria.items()),
    }
    return render(request, "reports/panel.html", contexto)


def exportar_csv(request):
    _verificar_formato("csv")
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="inventario.csv"'
    response.write("﻿")  # BOM para que Excel lea bien las tildes
    writer = csv.writer(response)
    writer.writerow(["Código", "Producto", "Categoría", "Precio", "Stock", "Valor total"])
    for p in Producto.objects.select_related("categoria"):
        writer.writerow([p.codigo, p.nombre, p.categoria.nombre, p.precio, p.stock, p.valor_total])
    return response


def exportar_pdf(request):
    _verificar_formato("pdf")
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except ImportError:
        return HttpResponse(
            "Para exportar a PDF instale reportlab: pip install reportlab",
            status=500,
        )

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, title="Reporte de inventario")
    estilos = getSampleStyleSheet()
    filas = [["Código", "Producto", "Categoría", "Precio", "Stock"]]
    for p in Producto.objects.select_related("categoria"):
        filas.append([p.codigo, p.nombre, p.categoria.nombre, f"$ {p.precio}", str(p.stock)])
    tabla = Table(filas, repeatRows=1)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3b73")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef2f9")]),
    ]))
    fecha = timezone.localtime().strftime("%d/%m/%Y %H:%M")
    doc.build([
        Paragraph("Reporte de inventario", estilos["Title"]),
        Paragraph(f"{settings.PRODUCT_NAME} - generado el {fecha}", estilos["Normal"]),
        Spacer(1, 12),
        tabla,
    ])
    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="inventario.pdf"'
    return response

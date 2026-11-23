from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("", views.panel, name="panel"),
    path("exportar/csv/", views.exportar_csv, name="exportar_csv"),
    path("exportar/pdf/", views.exportar_pdf, name="exportar_pdf"),
]

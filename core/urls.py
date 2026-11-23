from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.ProductoListView.as_view(), name="producto_list"),
    path("productos/nuevo/", views.ProductoCreateView.as_view(), name="producto_create"),
    path("productos/<int:pk>/editar/", views.ProductoUpdateView.as_view(), name="producto_update"),
]

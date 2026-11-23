from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("ingresar/", views.IngresarView.as_view(), name="login"),
    path("salir/", views.SalirView.as_view(), name="logout"),
    path("registro/", views.registro, name="registro"),
]

from django.urls import path

from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.NotificacionListView.as_view(), name="lista"),
    path("<int:pk>/leida/", views.marcar_leida, name="marcar_leida"),
]

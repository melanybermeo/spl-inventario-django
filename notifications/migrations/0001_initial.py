import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notificacion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("mensaje", models.CharField(max_length=255)),
                ("leida", models.BooleanField(default=False)),
                ("creada", models.DateTimeField(auto_now_add=True)),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notificaciones",
                        to="core.producto",
                    ),
                ),
            ],
            options={
                "verbose_name": "notificación",
                "verbose_name_plural": "notificaciones",
                "ordering": ["leida", "-creada"],
            },
        ),
    ]

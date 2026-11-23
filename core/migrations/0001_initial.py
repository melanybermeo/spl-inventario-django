import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=80, unique=True)),
            ],
            options={
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=120)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("stock_minimo", models.PositiveIntegerField(default=5)),
                ("creado", models.DateTimeField(auto_now_add=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="productos",
                        to="core.categoria",
                    ),
                ),
            ],
            options={"ordering": ["nombre"]},
        ),
    ]

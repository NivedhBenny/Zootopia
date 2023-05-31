# Generated by Django 4.2.1 on 2023-05-30 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("zootopia", "0020_cart_total"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="total",
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("petname", models.CharField(max_length=10)),
                ("photo", models.FileField(upload_to="")),
                ("price", models.CharField(max_length=10)),
                ("quantity", models.CharField(default="1", max_length=10)),
                ("total", models.CharField(max_length=10)),
                ("order_status", models.CharField(max_length=10)),
                (
                    "Pets",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zootopia.pets"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
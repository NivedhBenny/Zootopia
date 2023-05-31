# Generated by Django 4.2.1 on 2023-05-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("zootopia", "0028_cart_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="Products",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="zootopia.products",
            ),
        ),
    ]
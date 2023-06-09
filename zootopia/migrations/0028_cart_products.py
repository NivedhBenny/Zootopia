# Generated by Django 4.2.1 on 2023-05-30 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("zootopia", "0027_remove_cart_products"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="Products",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="zootopia.products",
            ),
        ),
    ]

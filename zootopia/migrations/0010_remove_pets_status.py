# Generated by Django 4.2.1 on 2023-05-29 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zootopia", "0009_pets_status_products_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pets",
            name="Status",
        ),
    ]

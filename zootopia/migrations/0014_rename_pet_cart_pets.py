# Generated by Django 4.2.1 on 2023-05-29 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zootopia", "0013_cart_pet"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="pet",
            new_name="PetS",
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zootopia", "0016_pay"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pay",
            old_name="productname",
            new_name="petsname",
        ),
    ]

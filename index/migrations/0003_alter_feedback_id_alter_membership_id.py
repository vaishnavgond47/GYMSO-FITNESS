# Generated by Django 4.2.4 on 2023-09-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("index", "0002_membership"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="membership",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

# Generated by Django 5.0.8 on 2024-08-18 13:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingAddress",
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
                ("full_name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("address1", models.CharField(max_length=255)),
                ("address2", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(blank=True, max_length=255, null=True)),
                ("zipcode", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shipping Adress",
            },
        ),
    ]

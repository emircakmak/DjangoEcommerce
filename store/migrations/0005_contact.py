# Generated by Django 5.0.8 on 2024-09-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_profile_old_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=40)),
                ("message", models.CharField(max_length=500)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
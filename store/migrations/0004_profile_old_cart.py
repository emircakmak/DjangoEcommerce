# Generated by Django 5.0.8 on 2024-08-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="old_cart",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 4.2 on 2025-01-30 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                ("description", models.TextField()),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
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

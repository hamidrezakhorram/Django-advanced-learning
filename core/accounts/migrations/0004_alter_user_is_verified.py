# Generated by Django 5.1.1 on 2025-03-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

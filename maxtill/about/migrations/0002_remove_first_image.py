# Generated by Django 5.0.2 on 2024-02-26 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="first",
            name="image",
        ),
    ]

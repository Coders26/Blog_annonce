# Generated by Django 5.0.2 on 2024-02-27 16:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("annonce", "0008_commentaire"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commentaire",
            name="email",
        ),
    ]
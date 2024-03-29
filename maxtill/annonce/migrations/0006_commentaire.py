# Generated by Django 5.0.2 on 2024-02-27 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("annonce", "0005_alter_annonce_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commentaire",
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
                ("nom", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("commentaire", models.TextField()),
                ("status", models.BooleanField(default=True)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                (
                    "annonce",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commentaire",
                        to="annonce.annonce",
                    ),
                ),
            ],
        ),
    ]

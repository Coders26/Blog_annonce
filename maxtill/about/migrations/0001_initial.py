# Generated by Django 5.0.2 on 2024-02-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="First",
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
                ("titre", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
                ("contenus", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Fourth",
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
                ("titre", models.CharField(max_length=50)),
                ("contenus", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Info",
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
                ("number", models.TextField()),
                ("mail", models.EmailField(max_length=254)),
                ("adresse", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Plus",
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
                ("lien", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Second",
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
                ("titre", models.CharField(max_length=50)),
                ("contenus", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Third",
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
                ("titre", models.CharField(max_length=50)),
                ("contenus", models.TextField()),
            ],
        ),
    ]

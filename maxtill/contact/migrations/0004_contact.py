# Generated by Django 5.0.2 on 2024-02-26 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0003_rename_info1_info"),
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
                ("nom", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("contenus", models.TextField()),
                ("active", models.BooleanField(default=False)),
                ("statuts", models.BooleanField(default=True)),
                ("date_add", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["date_add"],
            },
        ),
    ]

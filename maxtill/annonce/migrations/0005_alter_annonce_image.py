# Generated by Django 5.0.2 on 2024-02-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("annonce", "0004_alter_annonce_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="annonce",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]

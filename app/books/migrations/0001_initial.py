# Generated by Django 5.0 on 2023-12-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("author", models.CharField(max_length=100)),
                ("pages", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("publisher", models.CharField(max_length=100)),
                ("publication_date", models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-12-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamMembers",
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
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Last Name"),
                ),
                (
                    "phone",
                    models.CharField(max_length=100, verbose_name="Phone Number"),
                ),
                ("email", models.CharField(max_length=100, verbose_name="Email")),
                ("join", models.DateField(verbose_name="Joining Date")),
            ],
        ),
    ]

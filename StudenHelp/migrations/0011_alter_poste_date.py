# Generated by Django 4.2.13 on 2024-05-17 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("StudenHelp", "0010_alter_poste_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poste",
            name="date",
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
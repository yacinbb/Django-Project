# Generated by Django 5.0.2 on 2024-05-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudenHelp', '0002_reaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='poste',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.1.14 on 2022-02-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20220212_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Описание покемона'),
        ),
    ]

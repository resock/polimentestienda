# Generated by Django 3.2 on 2021-05-06 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_productomanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductoManager',
        ),
    ]
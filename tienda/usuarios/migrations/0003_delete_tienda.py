# Generated by Django 3.2 on 2021-05-05 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_delete_productos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tienda',
        ),
    ]
# Generated by Django 3.2 on 2021-05-05 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='iid',
            new_name='id',
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-22 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200421_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='Type',
            new_name='Type_advertisement',
        ),
        migrations.RenameField(
            model_name='phones',
            old_name='type',
            new_name='typePhone',
        ),
    ]

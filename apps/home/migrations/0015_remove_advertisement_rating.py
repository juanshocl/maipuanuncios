# Generated by Django 3.0.5 on 2020-04-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200425_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='rating',
        ),
    ]

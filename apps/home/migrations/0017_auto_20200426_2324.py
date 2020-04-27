# Generated by Django 3.0.5 on 2020-04-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200426_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='includes_maps',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='logo',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_advertisement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
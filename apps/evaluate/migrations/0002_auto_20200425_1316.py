# Generated by Django 3.0.5 on 2020-04-25 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
        ('home', '0015_remove_advertisement_rating'),
        ('evaluate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='User',
        ),
        migrations.AddField(
            model_name='ratings',
            name='UserRating',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.user'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='advertisementRating',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.advertisement'),
        ),
    ]

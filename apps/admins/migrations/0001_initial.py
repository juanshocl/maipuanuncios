# Generated by Django 3.0.5 on 2020-04-21 15:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_auto_20200421_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=14)),
                ('advertisement_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.advertisement')),
                ('role', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.roles')),
            ],
        ),
    ]

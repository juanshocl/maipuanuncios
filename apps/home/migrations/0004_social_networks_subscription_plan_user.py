# Generated by Django 3.0.5 on 2020-04-12 05:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200412_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription_plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('valid_from', models.DateField(auto_now=True)),
                ('valid_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='social_networks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('user_socialNetwork', models.CharField(max_length=50)),
                ('advertisement_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.advertisement')),
            ],
        ),
    ]
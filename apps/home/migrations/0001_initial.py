# Generated by Django 3.0.5 on 2020-04-09 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='credits',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_amount', models.IntegerField()),
                ('days', models.IntegerField()),
            ],
        ),
    ]

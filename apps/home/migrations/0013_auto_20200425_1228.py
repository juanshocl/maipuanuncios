# Generated by Django 3.0.5 on 2020-04-25 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200424_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='namesocialnetworks',
            old_name='user_socialNetwork',
            new_name='NameDescriptions',
        ),
        migrations.RenameField(
            model_name='social_networks',
            old_name='name',
            new_name='user_socialNetwork',
        ),
    ]

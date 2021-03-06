# Generated by Django 3.0.5 on 2020-04-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20200427_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='open_from',
            field=models.IntegerField(choices=[(1, '00:00'), (2, '00:30'), (3, '01:00'), (4, '01:30'), (5, '02:00'), (6, '02:30'), (7, '03:00'), (8, '03:30'), (9, '04:00'), (10, '04:30'), (11, '05:00'), (12, '05:30'), (13, '06:00'), (14, '06:30'), (15, '07:00'), (16, '07:30'), (17, '08:00'), (18, '08:30'), (19, '09:00'), (20, '09:30'), (21, '10:00'), (22, '10:30'), (23, '11:00'), (24, '11:30'), (25, '12:00'), (26, '12:30'), (27, '13:00'), (28, '13:30'), (29, '14:00'), (30, '14:30'), (31, '15:00'), (32, '15:30'), (31, '16:00'), (32, '16:30'), (19, '17:00'), (20, '17:30'), (21, '18:00'), (22, '18:30'), (23, '19:00'), (24, '19:30'), (25, '20:00'), (26, '20:30'), (27, '21:00'), (28, '21:30'), (29, '22:00'), (30, '22:30'), (31, '23:00'), (32, '23:30')], default=None),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='open_to',
            field=models.IntegerField(choices=[(1, '00:00'), (2, '00:30'), (3, '01:00'), (4, '01:30'), (5, '02:00'), (6, '02:30'), (7, '03:00'), (8, '03:30'), (9, '04:00'), (10, '04:30'), (11, '05:00'), (12, '05:30'), (13, '06:00'), (14, '06:30'), (15, '07:00'), (16, '07:30'), (17, '08:00'), (18, '08:30'), (19, '09:00'), (20, '09:30'), (21, '10:00'), (22, '10:30'), (23, '11:00'), (24, '11:30'), (25, '12:00'), (26, '12:30'), (27, '13:00'), (28, '13:30'), (29, '14:00'), (30, '14:30'), (31, '15:00'), (32, '15:30'), (31, '16:00'), (32, '16:30'), (19, '17:00'), (20, '17:30'), (21, '18:00'), (22, '18:30'), (23, '19:00'), (24, '19:30'), (25, '20:00'), (26, '20:30'), (27, '21:00'), (28, '21:30'), (29, '22:00'), (30, '22:30'), (31, '23:00'), (32, '23:30')], default=None),
        ),
    ]

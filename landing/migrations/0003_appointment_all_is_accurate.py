# Generated by Django 3.0 on 2021-02-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20210203_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='all_is_accurate',
            field=models.BooleanField(default=False),
        ),
    ]

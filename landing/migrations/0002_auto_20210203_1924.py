# Generated by Django 3.0 on 2021-02-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(choices=[('', 'Seleccione el día'), ('23 de febrero', '23 de febrero'), ('24 de febrero', '24 de febrero')], max_length=15),
        ),
    ]

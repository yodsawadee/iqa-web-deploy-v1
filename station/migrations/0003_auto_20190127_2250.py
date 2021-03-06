# Generated by Django 2.0 on 2019-01-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0002_auto_20190127_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reading',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reading',
            name='longitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reading',
            name='pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reading',
            name='temp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reading',
            name='wind_speed',
            field=models.IntegerField(),
        ),
    ]

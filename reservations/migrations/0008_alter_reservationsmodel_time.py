# Generated by Django 5.0.6 on 2024-05-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_alter_reservationsmodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationsmodel',
            name='time',
            field=models.TimeField(verbose_name='H:i'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0009_alter_reservation_received_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='reservation_received',
            constraint=models.UniqueConstraint(fields=('date', 'time', 'table_number'), name='unique_reserve'),
        ),
    ]

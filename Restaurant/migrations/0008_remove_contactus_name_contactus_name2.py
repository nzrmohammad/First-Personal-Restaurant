# Generated by Django 4.0.3 on 2022-03-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0007_alter_reservation_received_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='name',
        ),
        migrations.AddField(
            model_name='contactus',
            name='name2',
            field=models.CharField(default='', max_length=35, verbose_name='name'),
            preserve_default=False,
        ),
    ]
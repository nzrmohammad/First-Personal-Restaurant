# Generated by Django 4.0.3 on 2022-04-05 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0008_remove_contactus_name_contactus_name2'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation_received',
            unique_together=set(),
        ),
    ]

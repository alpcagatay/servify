# Generated by Django 4.0.1 on 2022-01-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0011_remove_event_venue_remove_service_venue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='lng',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0 on 2022-01-28 14:06

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_event_cityname_event_location_service_cityname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]

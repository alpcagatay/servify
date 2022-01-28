# Generated by Django 4.0 on 2022-01-27 18:09

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='parent_place',
        ),
        migrations.AddField(
            model_name='place',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='Ankara', max_length=63),
        ),
    ]

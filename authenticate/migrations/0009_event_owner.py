# Generated by Django 3.2.11 on 2022-01-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0008_service_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Event Owner'),
        ),
    ]
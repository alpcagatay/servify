# Generated by Django 3.2.11 on 2022-01-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
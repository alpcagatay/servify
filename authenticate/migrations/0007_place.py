# Generated by Django 3.2.11 on 2022-01-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_alter_feed_feed_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('parent_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.place')),
            ],
        ),
    ]

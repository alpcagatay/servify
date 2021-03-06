# Generated by Django 3.2.11 on 2022-01-26 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20220126_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='service',
        ),
        migrations.AddField(
            model_name='comment',
            name='eventcom',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecomments', to='authenticate.event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='servicecom',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scomments', to='authenticate.service'),
        ),
    ]

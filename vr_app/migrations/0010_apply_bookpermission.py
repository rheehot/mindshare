# Generated by Django 2.2.3 on 2019-08-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_app', '0009_profile2_mileage'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='BookPermission',
            field=models.IntegerField(blank=True, default=0, max_length=10),
        ),
    ]

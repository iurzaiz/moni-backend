# Generated by Django 3.0 on 2022-04-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

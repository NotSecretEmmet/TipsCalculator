# Generated by Django 3.1 on 2020-11-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_profile_locatie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='locatie',
            field=models.CharField(choices=[('CS', 'CS'), ('ZUID', 'ZUID')], default='CS', max_length=30),
        ),
    ]

# Generated by Django 3.1.6 on 2022-07-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GotchaSys', '0009_auto_20220707_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='storylines',
            name='Chapter_Name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

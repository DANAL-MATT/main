# Generated by Django 3.1.6 on 2022-07-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GotchaSys', '0014_auto_20220708_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='gacha',
            name='Banner_Name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='gacha',
            name='Banner_ID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

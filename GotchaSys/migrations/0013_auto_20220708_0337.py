# Generated by Django 3.1.6 on 2022-07-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GotchaSys', '0012_auto_20220707_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='Character_Rarity',
            field=models.CharField(max_length=5),
        ),
    ]
# Generated by Django 3.1.6 on 2022-07-07 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GotchaSys', '0010_storylines_chapter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='Character_Name',
            field=models.CharField(default='', max_length=35),
        ),
    ]

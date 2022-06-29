# Generated by Django 3.1.6 on 2022-05-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GotchaSys', '0003_auto_20220421_0524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text1',
            new_name='email',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='query',
            field=models.TextField(default=''),
        ),
    ]

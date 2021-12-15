# Generated by Django 3.2.7 on 2021-11-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0011_alter_housingoption_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housingoption',
            name='photo',
        ),
        migrations.AddField(
            model_name='housingoption',
            name='pic',
            field=models.URLField(default='https://i.stack.imgur.com/y9DpT.jpg'),
        ),
    ]

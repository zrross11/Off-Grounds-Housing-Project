# Generated by Django 3.2.7 on 2021-11-02 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0005_auto_20211102_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.CharField(default='', max_length=300),
        ),
    ]

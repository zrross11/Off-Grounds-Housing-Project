# Generated by Django 3.2.7 on 2021-11-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0013_rename_score_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingoption',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='housingoption',
            name='pic',
            field=models.URLField(default='https://cdn-icons-png.flaticon.com/128/2101/2101126.png'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0010_housingoption_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingoption',
            name='photo',
            field=models.ImageField(blank=True, upload_to='housing_images'),
        ),
    ]
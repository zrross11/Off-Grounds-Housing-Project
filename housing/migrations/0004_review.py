# Generated by Django 3.2.7 on 2021-11-02 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_remove_housingoption_housing_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='housing.housingoption')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

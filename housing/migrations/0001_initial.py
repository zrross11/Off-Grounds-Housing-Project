# Generated by Django 3.2.7 on 2021-10-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=1000)),
                ('numberOfBedrooms', models.IntegerField(default=0)),
                ('numberOfBathrooms', models.IntegerField(default=0)),
                ('pricePerUnit', models.IntegerField(default=0)),
                ('furnished', models.BooleanField(default=False)),
            ],
        ),
    ]
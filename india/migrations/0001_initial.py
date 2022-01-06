# Generated by Django 4.0.1 on 2022-01-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverallData',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('total_confirmed', models.BigIntegerField()),
                ('daily_confirmed', models.BigIntegerField()),
                ('total_recovered', models.BigIntegerField()),
                ('daily_recovered', models.BigIntegerField()),
                ('total_deceased', models.BigIntegerField()),
                ('daily_deceased', models.BigIntegerField()),
            ],
        ),
    ]

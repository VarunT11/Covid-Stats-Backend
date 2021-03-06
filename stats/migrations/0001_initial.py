# Generated by Django 4.0.1 on 2022-02-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_store_link', models.CharField(default='', max_length=400)),
                ('about_content', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('region_code_who', models.CharField(default='', max_length=10)),
                ('region_name_who', models.CharField(default='', max_length=100)),
                ('country_code', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('country_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CovidStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_type', models.CharField(default='', max_length=10)),
                ('region_code_who', models.CharField(default='', max_length=10)),
                ('region_name_who', models.CharField(default='', max_length=100)),
                ('country_code', models.CharField(default='', max_length=10)),
                ('country_name', models.CharField(default='', max_length=100)),
                ('state_code', models.CharField(default='', max_length=5)),
                ('state_name', models.CharField(default='', max_length=100)),
                ('district_name', models.CharField(default='', max_length=100)),
                ('date_of_stat', models.DateTimeField()),
                ('total_confirmed', models.BigIntegerField(default=0)),
                ('daily_confirmed', models.BigIntegerField(default=0)),
                ('total_recovered', models.BigIntegerField(default=0)),
                ('daily_recovered', models.BigIntegerField(default=0)),
                ('total_deceased', models.BigIntegerField(default=0)),
                ('daily_deceased', models.BigIntegerField(default=0)),
                ('total_active', models.BigIntegerField(default=0)),
                ('daily_active', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('source_name', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('source_description', models.CharField(default='', max_length=400)),
                ('source_url', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=100)),
                ('tags', models.CharField(default='', max_length=400)),
                ('linkedin', models.CharField(default='', max_length=400)),
                ('behance', models.CharField(default='', max_length=400)),
                ('github', models.CharField(default='', max_length=400)),
                ('mail', models.CharField(default='', max_length=400)),
                ('image_url', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_type', models.CharField(default='', max_length=10)),
                ('source_name', models.CharField(default='', max_length=50)),
                ('authors', models.CharField(default='', max_length=300)),
                ('title', models.CharField(default='', max_length=300)),
                ('description', models.CharField(default='', max_length=1000)),
                ('news_url', models.CharField(default='', max_length=400)),
                ('news_image_url', models.CharField(default='', max_length=400)),
                ('published_time', models.DateTimeField()),
                ('content', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('india_news_last_updated_time', models.DateTimeField(null=True)),
                ('world_news_last_updated_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateInfo',
            fields=[
                ('state_code', models.CharField(default='', max_length=5, primary_key=True, serialize=False)),
                ('state_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadSafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhoRegionInfo',
            fields=[
                ('region_code_who', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('region_name_who', models.CharField(default='', max_length=100)),
            ],
        ),
    ]

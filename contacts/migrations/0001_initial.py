# Generated by Django 2.2.6 on 2019-11-21 03:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('listing_slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the upto 10 digits', regex='^\\d{8,10}$')])),
                ('message', models.TextField(blank=True, max_length=100)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]

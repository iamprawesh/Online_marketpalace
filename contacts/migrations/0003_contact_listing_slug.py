# Generated by Django 2.2.6 on 2019-11-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contact_listing_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='listing_slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
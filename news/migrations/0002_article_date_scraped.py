# Generated by Django 3.0.2 on 2020-01-09 01:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_scraped',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

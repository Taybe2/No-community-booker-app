# Generated by Django 4.2.16 on 2024-11-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_centre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitycentre',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

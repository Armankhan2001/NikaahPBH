# Generated by Django 5.0.3 on 2024-04-04 00:27

import PBH.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBH', '0017_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=PBH.models.default_profile_image, null=True, upload_to=''),
        ),
    ]
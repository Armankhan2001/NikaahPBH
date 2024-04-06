# Generated by Django 5.0.3 on 2024-04-03 21:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBH', '0009_alter_profile_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinLengthValidator(10, message='Contact number must be at least 10 digits.'), django.core.validators.MaxLengthValidator(13, message='Contact number must be at most 13 digits.')]),
        ),
    ]
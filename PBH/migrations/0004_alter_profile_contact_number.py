# Generated by Django 5.0.3 on 2024-04-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBH', '0003_profile_contact_number_profile_instagram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(default='0', max_length=15, unique=True),
        ),
    ]
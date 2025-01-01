# Generated by Django 5.1.4 on 2025-01-01 06:49

import adminAuth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAuth', '0004_customuser_first_name_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='adminProfileImage/', validators=[adminAuth.models.validate_file_size]),
            preserve_default=False,
        ),
    ]
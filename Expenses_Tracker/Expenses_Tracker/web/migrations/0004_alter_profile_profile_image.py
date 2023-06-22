# Generated by Django 4.2.2 on 2023-06-22 09:10

import Expenses_Tracker.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='/static/images/user.png', null=True, upload_to='profiles/', validators=[Expenses_Tracker.web.models.validate_image_size]),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-29 08:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_system_app', '0006_remove_group_max_users_remove_group_min_users_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='UserGroup',
        ),
    ]

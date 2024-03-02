# Generated by Django 5.0.2 on 2024-03-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_system_app', '0011_alter_lesson_name_alter_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='max_users',
        ),
        migrations.RemoveField(
            model_name='product',
            name='min_users',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='max_users',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='min_users',
            field=models.PositiveIntegerField(default=5),
        ),
    ]

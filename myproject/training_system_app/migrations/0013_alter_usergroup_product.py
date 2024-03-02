# Generated by Django 5.0.2 on 2024-03-02 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_system_app', '0012_remove_product_max_users_remove_product_min_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='training_system_app.product'),
        ),
    ]
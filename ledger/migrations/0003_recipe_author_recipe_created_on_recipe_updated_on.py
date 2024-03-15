# Generated by Django 5.0.2 on 2024-03-15 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipe_options_alter_recipeingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.CharField(default='author', max_length=50),
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

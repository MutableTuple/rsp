# Generated by Django 4.2.14 on 2024-08-01 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_fooditem_ingredients_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='foodItem',
        ),
    ]

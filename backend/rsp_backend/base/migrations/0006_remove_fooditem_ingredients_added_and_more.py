# Generated by Django 4.2.14 on 2024-08-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_fooditem_ingredients_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='ingredients_added',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='ingredients_added',
            field=models.ManyToManyField(blank=True, null=True, to='base.ingredients'),
        ),
    ]

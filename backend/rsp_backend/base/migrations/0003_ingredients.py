# Generated by Django 4.2.14 on 2024-08-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_fooditem_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(blank=True, max_length=2500, null=True)),
                ('foodItem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.fooditem')),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]

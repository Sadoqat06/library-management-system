# Generated by Django 5.1.4 on 2024-12-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='rental_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

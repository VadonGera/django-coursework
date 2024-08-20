# Generated by Django 5.1 on 2024-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique_first_name_last_name'),
        ),
    ]

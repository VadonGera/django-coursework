# Generated by Django 5.1 on 2024-08-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('todolist', '0003_alter_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]

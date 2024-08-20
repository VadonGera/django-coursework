# Generated by Django 5.1 on 2024-08-17 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('todolist', '0002_category_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='todolist.category', verbose_name='Категория'),
        ),
    ]

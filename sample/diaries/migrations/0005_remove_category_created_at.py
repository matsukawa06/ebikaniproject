# Generated by Django 2.2.15 on 2020-08-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0004_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
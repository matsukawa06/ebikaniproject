# Generated by Django 2.2.15 on 2020-08-22 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='カテゴリ')),
                ('text', models.TextField(verbose_name='本文')),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]

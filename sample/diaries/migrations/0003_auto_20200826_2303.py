# Generated by Django 2.2.15 on 2020-08-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_auto_20200826_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.AlterField(
            model_name='diary',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='diaries.Category', verbose_name='カテゴリ'),
        ),
    ]

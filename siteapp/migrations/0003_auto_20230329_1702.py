# Generated by Django 3.2.18 on 2023-03-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0002_auto_20230329_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorcase',
            name='error_01',
            field=models.BooleanField(verbose_name='異常０１'),
        ),
        migrations.AlterField(
            model_name='errorcase',
            name='error_02',
            field=models.BooleanField(verbose_name='異常０２'),
        ),
        migrations.AlterField(
            model_name='errorcase',
            name='error_03',
            field=models.BooleanField(verbose_name='異常０３'),
        ),
    ]

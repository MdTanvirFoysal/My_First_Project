# Generated by Django 2.2.5 on 2020-11-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20201101_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Name Of First'),
        ),
    ]

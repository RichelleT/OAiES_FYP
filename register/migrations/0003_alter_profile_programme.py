# Generated by Django 3.2 on 2022-02-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20220209_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='programme',
            field=models.TextField(blank=True, default='', max_length=150),
        ),
    ]
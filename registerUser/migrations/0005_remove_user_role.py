# Generated by Django 3.2 on 2022-02-07 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerUser', '0004_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]

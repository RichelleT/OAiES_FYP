# Generated by Django 3.2 on 2022-02-08 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('register', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]
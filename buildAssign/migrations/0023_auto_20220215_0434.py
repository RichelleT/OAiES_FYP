# Generated by Django 3.2 on 2022-02-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0022_answer_set_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='set_added',
        ),
        migrations.AddField(
            model_name='assignment',
            name='set_added',
            field=models.BooleanField(default=False),
        ),
    ]
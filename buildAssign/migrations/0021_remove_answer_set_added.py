# Generated by Django 3.2 on 2022-02-14 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0020_alter_answer_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='set_added',
        ),
    ]

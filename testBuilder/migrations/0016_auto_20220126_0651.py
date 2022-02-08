# Generated by Django 3.2 on 2022-01-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0015_auto_20220125_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='correct',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='percentage',
            field=models.IntegerField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='total',
            field=models.IntegerField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='wrong',
            field=models.IntegerField(default='', max_length=10),
        ),
    ]

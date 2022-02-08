# Generated by Django 3.2 on 2022-01-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0008_auto_20220122_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
        migrations.AlterField(
            model_name='test',
            name='test_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

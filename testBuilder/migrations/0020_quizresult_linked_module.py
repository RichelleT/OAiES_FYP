# Generated by Django 3.2 on 2022-02-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0019_remove_quizresult_linked_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='linked_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testBuilder.module'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('start', 'Start'), ('in_process', 'In Process'), ('finish', 'Finish')], default='start'),
        ),
    ]

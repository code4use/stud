# Generated by Django 2.2.1 on 2019-05-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20190520_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_head',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-20 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=50)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField()),
                ('task_solv', models.TextField()),
                ('task_num_answer', models.FloatField(blank=True, default=0.0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.SubjectSection')),
            ],
        ),
    ]

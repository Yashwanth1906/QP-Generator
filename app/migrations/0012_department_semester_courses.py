# Generated by Django 4.2.4 on 2024-02-27 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_questions_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_no', models.IntegerField(primary_key=True, serialize=False)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200)),
                ('semester_no', models.IntegerField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]

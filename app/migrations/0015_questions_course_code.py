# Generated by Django 4.2.4 on 2024-02-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_semesters'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='course_code',
            field=models.CharField(default='', max_length=50),
        ),
    ]
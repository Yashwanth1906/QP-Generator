# Generated by Django 4.2.4 on 2024-01-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='Type',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='questions',
            name='difficulty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questions',
            name='question',
            field=models.TextField(default=''),
        ),
    ]

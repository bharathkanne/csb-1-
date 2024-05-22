# Generated by Django 5.0.1 on 2024-05-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_logentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.EmailField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
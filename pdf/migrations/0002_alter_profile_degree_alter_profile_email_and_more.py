# Generated by Django 5.1.3 on 2024-12-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='previous_work',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='summary',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 2.2 on 2019-04-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default='', max_length=128),
        ),
    ]

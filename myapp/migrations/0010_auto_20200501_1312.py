# Generated by Django 3.0.5 on 2020-05-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200501_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(upload_to='Profile/'),
        ),
    ]

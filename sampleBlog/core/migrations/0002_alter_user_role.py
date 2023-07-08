# Generated by Django 4.2.3 on 2023-07-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Administrator', 'Admin'), ('Moderator', 'Moderator')], default='User', max_length=15),
        ),
    ]
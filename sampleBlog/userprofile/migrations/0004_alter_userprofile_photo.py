# Generated by Django 4.2.3 on 2023-08-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='d1.png', upload_to='images/user_profile'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_category_category_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]

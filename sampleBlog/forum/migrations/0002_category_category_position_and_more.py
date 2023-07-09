# Generated by Django 4.2.3 on 2023-07-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_position',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='subcategory_position',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='topic',
            name='pinned',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=2),
        ),
    ]
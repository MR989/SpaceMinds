# Generated by Django 3.0.5 on 2020-05-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200528_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content_sub_head2',
            field=models.TextField(default='', max_length=500),
        ),
    ]

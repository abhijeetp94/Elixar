# Generated by Django 3.1.1 on 2020-09-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayApp', '0004_auto_20200906_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='conqueresub',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='explorersub',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-06 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(default='INR', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('school', models.CharField(max_length=50)),
                ('courseapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PayApp.course')),
            ],
        ),
        migrations.CreateModel(
            name='FreeTrialSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PayApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ExplorerSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PayApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ConquereSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PayApp.student')),
            ],
        ),
    ]
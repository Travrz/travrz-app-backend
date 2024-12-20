# Generated by Django 5.1.4 on 2024-12-20 15:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('profile_pic_url', models.URLField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Climb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climb_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('media_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0)),
                ('private', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='core.tag')),
            ],
        ),
    ]

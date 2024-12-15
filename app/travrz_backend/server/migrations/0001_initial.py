# Generated by Django 5.1.4 on 2024-12-15 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("score", models.IntegerField(default=0)),
                ("profile_pic_url", models.URLField(blank=True)),
                ("bio", models.TextField(blank=True)),
                ("location", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Climb",
            fields=[
                ("climb_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("grade", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("media_url", models.URLField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("rating", models.FloatField(default=0)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="server.user"
                    ),
                ),
            ],
        ),
    ]
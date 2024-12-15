from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    profile_pic_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

class Climb(models.Model):
    climb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    description = models.TextField()
    media_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

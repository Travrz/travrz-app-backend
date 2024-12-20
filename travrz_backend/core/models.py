from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, username, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username, and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Custom User model."""

    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    score = models.IntegerField(default=0)
    profile_pic_url = models.URLField(blank=True)

    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # for now we'll say yes to everything
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # for now we'll say yes to everything
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Climb(models.Model):
    """Climb object."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    climb_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    description = models.TextField()
    media_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)

    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    """Tags for filtering climbs."""

    tag_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

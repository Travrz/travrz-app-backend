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

    class Grade(models.TextChoices):
        """Enum for climb grades."""

        # indoor
        V0 = "V0", "V0"
        V1 = "V1", "V1"
        V2 = "V2", "V2"
        V3 = "V3", "V3"
        V4 = "V4", "V4"
        V5 = "V5", "V5"
        V6 = "V6", "V6"
        V7 = "V7", "V7"
        V8 = "V8", "V8"
        V9 = "V9", "V9"
        V10 = "V10", "V10"
        V11 = "V11", "V11"
        V12 = "V12", "V12"
        V13 = "V13", "V13"
        V14 = "V14", "V14"
        V15 = "V15", "V15"
        V16 = "V16", "V16"
        V17 = "V17", "V17"
        V18 = "V18", "V18"

        # outdoor
        F5_5 = "5.5", "5.5"
        F5_6 = "5.6", "5.6"
        F5_7 = "5.7", "5.7"
        F5_8 = "5.8", "5.8"
        F5_9 = "5.9", "5.9"
        F5_10a = "5.10a", "5.10a"
        F5_10b = "5.10b", "5.10b"
        F5_10c = "5.10c", "5.10c"
        F5_10d = "5.10d", "5.10d"
        F5_11a = "5.11a", "5.11a"
        F5_11b = "5.11b", "5.11b"
        F5_11c = "5.11c", "5.11c"
        F5_11d = "5.11d", "5.11d"
        F5_12a = "5.12a", "5.12a"
        F5_12b = "5.12b", "5.12b"
        F5_12c = "5.12c", "5.12c"
        F5_12d = "5.12d", "5.12d"
        F5_13a = "5.13a", "5.13a"
        F5_13b = "5.13b", "5.13b"
        F5_13c = "5.13c", "5.13c"
        F5_13d = "5.13d", "5.13d"
        F5_14a = "5.14a", "5.14a"
        F5_14b = "5.14b", "5.14b"
        F5_14c = "5.14c", "5.14c"
        F5_14d = "5.14d", "5.14d"
        F5_15a = "5.15a", "5.15a"
        F5_15b = "5.15b", "5.15b"
        F5_15c = "5.15c", "5.15c"
        F5_15d = "5.15d", "5.15d"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    climb_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    description = models.TextField()
    media_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    private = models.BooleanField(default=False)

    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    """Tags for filtering climbs."""

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

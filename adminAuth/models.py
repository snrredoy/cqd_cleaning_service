from django.db import models
from django.contrib.auth.models import AbstractBaseUser  , PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError

from .managers import CustomUserManager

# Create your models here.

def validate_file_size(value):
    filesize = value.size
    limit = 1 * 1024 * 1024  # 1MB in bytes
    if filesize > limit:
        raise ValidationError("Maximum file size is 1MB")
    




class CustomUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(upload_to='adminProfileImage/',validators=[validate_file_size], blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email
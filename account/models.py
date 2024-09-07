from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone=None, password=None, **other_fields):
        if email is None:
            raise ValueError("Email cannot be empty")
        user = self.model(email=self.normalize_email(email), phone=phone, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone=None, password=None, **other_fields):
        user = self.create_user(email, phone, password, **other_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractUser):
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=512, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    user_type = models.CharField(max_length=20, default='customer', choices=(
        ('admin', 'Admin User'),
        ('customer', 'Customer'),
    ))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', 'address', 'avatar']
    EMAIL_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name
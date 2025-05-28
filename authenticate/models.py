from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid

class UserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)  # hashes the password
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  ROLES = {
    'admin': 'Admin',
    'author': 'Author',
    'reader': 'Reader',
  }

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20, choices=ROLES, default='reader')
  created_at = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  objects = UserManager()

  def __str__(self):
    return f'{self.username} ({self.role})'

  class Meta:
    db_table = 'users'
    ordering = ['-created_at']
    verbose_name = 'User'
    indexes = [
      models.Index(fields=['username'], name='username_idx'),
      models.Index(fields=['email'], name='email_idx'),
    ]

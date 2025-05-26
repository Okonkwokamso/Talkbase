from django.db import models

class User(models.Model):
  ROLES = {
    'admin': 'Admin',
    'author': 'Author',
    'reader': 'Reader',
  }
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=128) 
  role = models.CharField(max_length=20, choices=ROLES, default='reader')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


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

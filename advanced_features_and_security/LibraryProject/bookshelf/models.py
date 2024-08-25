from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
  def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self, username, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(null=True, blank=True)
  
  objects = CustomUserManager()
  
  def __str(self):
    return f'{self.date_of_birth}'

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()
  
  class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
            ('can_list', 'Can list book'),
        ]

  def __str__(self):
    return self.title
  
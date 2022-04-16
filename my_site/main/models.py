from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(null=True, blank=True)
    university = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    group = models.CharField(max_length=30, null=True, blank=True)

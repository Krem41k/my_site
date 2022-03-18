from django.db import models

from main.models import CustomUser


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    grade = models.IntegerField()

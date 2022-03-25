from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from main.models import CustomUser


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    grade = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

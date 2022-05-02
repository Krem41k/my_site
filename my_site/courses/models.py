from django.db import models

from main.models import CustomUser


class Course(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    content = models.TextField()
    material = models.FileField(upload_to="study_materials/%Y/%m/%d/")

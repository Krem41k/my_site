from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    document = models.FileField(upload_to="files/%Y/%m/%d/")

from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    uploadedFile = models.FileField(upload_to="Uploaded Files/")

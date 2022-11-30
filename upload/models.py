from django.db import models

class FileModel(models.Model):
    upload = models.FileField(upload_to='')
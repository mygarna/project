from django.db import models

class Dictionary(models.Model):
    english = models.CharField(max_length=256)
    spanish = models.CharField(max_length=256)
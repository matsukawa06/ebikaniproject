from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)


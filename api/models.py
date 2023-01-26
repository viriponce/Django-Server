from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resource(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False, unique=True)
    edit_link = models.CharField(max_length=255, null=False, blank=False)
    published_link = models.CharField(max_length=255, null=False, blank=False)

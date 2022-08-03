from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.TextField()
    content = models.TextField()
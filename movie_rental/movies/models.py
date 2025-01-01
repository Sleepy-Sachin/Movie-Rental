# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image_url = models.URLField()# Add the library field
    available = models.BooleanField(default=True)


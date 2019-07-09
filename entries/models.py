from django.db import models

class Entries(models.Model):
    title = models.TextField()
    user = models.TextField(default='anonymous')
    entry = models.TextField()
from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def alt_text(self):
        return self.summary[:25]

    def __str__(self):
        return self.summary[:50]+"..."

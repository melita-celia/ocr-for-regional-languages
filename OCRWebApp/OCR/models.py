from django.db import models

# Create your models here.
class Ocr(models.Model):
    image = models.ImageField(upload_to='images/')
    
class AudioFile(models.Model):
    obj = models.FileField(upload_to="static/audio/")

from django.db import models

class Gesture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gestures/')

    def __str__(self):
        return self.name
# Create your models here.

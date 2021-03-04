from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    exp = models.CharField(max_length=100)
    dir = models.CharField(max_length=15)
    act = models.CharField(max_length=30)
    year = models.IntegerField()
    image = models.ImageField(default = '')

    def __str__(self):
        return self.title

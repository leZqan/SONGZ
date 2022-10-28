from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name+self.last_name


class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_released = models.DateField(auto_now_add=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

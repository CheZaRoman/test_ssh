from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    test_field = models.TextField(blank=True)


class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



class Statistic(models.Model):
    result = models.JSONField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return "Statistic|{}".format(self.email)


# author = Author(name='John', date_created='2020-10-10')
# author.save()
# song = Song(title='1', author=author)
# song.save()

# songs = Song.objects.filter(author=author)

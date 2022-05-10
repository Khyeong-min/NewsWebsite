from django.db import models


# Create your models here.
class Comment(models.Model):
    idNews = models.CharField(max_length=10)
    nick = models.CharField(max_length=45)
    text = models.TextField()

    class Meta:
        db_table = 'comment'
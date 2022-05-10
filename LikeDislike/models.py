from django.db import models

# Create your models here.
class LikeDislike(models.Model):
    idNews = models.CharField(max_length=10)
    Likes = models.CharField(max_length=45)
    Dislikes = models.CharField(max_length=45)

    class Meta:
        db_table = 'likedislike'
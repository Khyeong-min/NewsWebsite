from django.db import models

# Create your models here.
class News(models.Model):
    idNews = models.CharField(max_length=10)
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=45)
    PublishDate = models.DateTimeField(auto_now_add=True)
    Text = models.TextField()
    Newspaper = models.CharField(max_length=45)
    Keyword = models.CharField(max_length=45, default=0)


    class Meta:
        db_table = 'news'
from django.db import models


class NB(models.Model):
        newspaper = models.TextField()
        sub_total = models.IntegerField()


#최종 이미지
class Result(models.Model):
        img_NB = models.ImageField(blank=True)


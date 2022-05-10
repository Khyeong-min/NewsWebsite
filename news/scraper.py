import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsWeb.settings")
import django
django.setup()


from news import models

f = open('News.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    models.News.objects.create(
        idNews=line[1],
        Title=line[2],
        Author=line[3],
        PublishDate=line[4],
        Text=line[5],
        Newspaper=line[7],
        Keyword=line[8],
        )
f.close()
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsWeb.settings")

import django
django.setup()

from LikeDislike import models

f = open('LikeDislike.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    models.LikeDislike.objects.create(
        idNews=line[1],
        Likes=line[2],
        Dislikes=line[3],
        )
f.close()
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsWeb.settings")

import django
django.setup()

from comment import models

f = open('comment.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    models.Comment.objects.create(
        idNews=line[1],
        nick=line[2],
        text=line[3],
        )
f.close()

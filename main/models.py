from django.db import models


class Urls(models.Model):
    url = models.TextField()
    identifier = models.TextField()
    counter = models.IntegerField()




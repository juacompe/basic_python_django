from django.db import models

class Competitor(models.Model):
    name = models.TextField()
    nick_name = models.TextField()
    no = models.IntegerField(unique=True)


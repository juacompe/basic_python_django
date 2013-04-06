from django.db import models

class Competitor(models.Model):
    name = models.TextField()
    nick_name = models.TextField()
    no = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.name

class Vote(models.Model):
    competitor = models.ForeignKey(Competitor, related_name='votes')
    

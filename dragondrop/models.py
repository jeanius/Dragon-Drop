from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Folder(models.Model):
    foldername = models.CharField(max_length=128, null=False)
    fusername_fk = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.foldername

class Bookmark(models.Model):
    url = models.URLField(unique=True)
    btitle = models.CharField(max_length=128, null=True)
    bdescr = models.CharField(max_length=1024, null=True)
    fname = models.ManyToManyField(Folder)
    saved_times = models.IntegerField(default=0)

    def __unicode__(self):
        return self.url
        
class BinFolder(models.Model):
    busername_fk = models.ForeignKey(User)
    bbmID_fk = models.ManyToManyField(Bookmark, blank=True, null=True)
    
    def __unicode__(self):
        return self.busername_fk.username



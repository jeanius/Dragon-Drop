from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from urlparse import urlparse
from dragondrop.get_domain_from_url import getDomain
from dragondrop.url_utilities import get_youtube_id

class Folder(models.Model):
    foldername = models.CharField(max_length=128, null=False)
    fusername_fk = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.foldername

class Bookmark(models.Model):
    url = models.URLField(unique=True)
    btitle = models.CharField(max_length=128, null=True, unique=False)
    bdescr = models.CharField(max_length=1024, null=True, unique=False)
    #bdomain = models.CharField(max_length=256, null=True, unique=False)
    fname = models.ManyToManyField(Folder, through='BookmarkToFolder')  #, through_fields=('folder', 'bookmark'))
    saved_times = models.IntegerField(default=0)

    def bdomain(self):
        return getDomain(self.url)
        
        
    def video_id(self):
        return get_youtube_id(self.url, self.bdomain())

    def niceName(self):
        return self.btitle or self.url       
    
    def __unicode__(self):
        return self.url

class BookmarkToFolder(models.Model):
    bffolder = models.ForeignKey(Folder)
    bfbookmark = models.ForeignKey(Bookmark)
    bfrank = models.IntegerField(default=0)

        
class BinFolder(models.Model):
    busername_fk = models.ForeignKey(User)
    bbmID_fk = models.ManyToManyField(Bookmark, blank=True, null=True)
    
    def __unicode__(self):
        return self.busername_fk.username
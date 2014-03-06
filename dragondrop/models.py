from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from urlparse import urlparse

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

# Given a URL (e.g. http://www.bing.com/images), this function returns the domain
# (e.g. bing.com). It's could probably be improved but hopefully works reasonably well.
def getDomain(url):
    domain = urlparse(url).netloc
    domain_parts = domain.split('.')
    if domain_parts[0] == "www":
        return '.'.join(domain_parts[1:])
    else:
        return domain
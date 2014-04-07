from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from urlparse import urlparse
from dragondrop.get_domain_from_url import getDomain
from dragondrop.url_utilities import get_youtube_id
import pickle

MAX_HISTORY_LENGTH = 30
MAX_POPULAR_LENGTH = 30
MAX_RECENTLY_ADDED_LENGTH = 30

class Folder(models.Model):
    foldername = models.CharField(max_length=128, null=False)
    fusername_fk = models.ForeignKey(User)

    def __unicode__(self):
        return self.foldername

class Bookmark(models.Model):
    url = models.URLField(unique=True)
    btitle = models.CharField(max_length=128, null=True, unique=False)
    bdescr = models.CharField(max_length=1024, null=True, unique=False)
    fname = models.ManyToManyField(Folder, through='BookmarkToFolder')
    saved_times = models.IntegerField(default=0)

    def bdomain(self):
        return getDomain(self.url)


    def video_id(self):
        return get_youtube_id(self.url, self.bdomain())

    def niceName(self):
        if self.btitle=="--- Title not found ---" or not self.btitle:
            return self.url
        return self.btitle

    def __unicode__(self):
        return self.url

class UserProfile(models.Model):
    histories = models.TextField(null=True)
    popular = models.TextField(null=True)
    recently_added = models.TextField(null=True)
    user = models.ForeignKey(User)

    def get_history(self):
        return pickle.loads(self.histories)

    def get_popular(self):
        return pickle.loads(self.popular)

    def get_recently_added(self):
        return pickle.loads(self.recently_added)

    def __add_to_dictionary(self,field_inst,result,field_length):
        """
        result: is a dictionary containing the title, url, ...

        this function adds as result to history;
        to do this it's gonna save this back to data base
        """

        # 1. get history and unpickle it

        if self.__dict__[field_inst] is None:
            field_val = ""
            hl = []
        else:
            field_val = self.__dict__[field_inst]
            hl = pickle.loads(field_val)

        lngth = len(hl)

        if lngth == field_length:
            hl.pop()

        hl.insert(0,result)
        self.__dict__[field_inst] = pickle.dumps(hl)

    def add_to_recently_added(self, result):
        self.__add_to_dictionary('recently_added', result, MAX_RECENTLY_ADDED_LENGTH)

    def add_to_history(self, result):
        self.__add_to_dictionary('histories', result, MAX_HISTORY_LENGTH)

    def add_to_popular(self, result):
        self.__add_to_dictionary('popular', result, MAX_POPULAR_LENGTH)



class BookmarkToFolder(models.Model):
    bffolder = models.ForeignKey(Folder)
    bfbookmark = models.ForeignKey(Bookmark)
    bfrank = models.FloatField(default=0)
    datecreated = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

class BinFolder(models.Model):
    busername_fk = models.OneToOneField(User)
    bbmID_fk = models.ManyToManyField(Bookmark, blank=True, null=True)

    def __unicode__(self):
        return self.busername_fk.username
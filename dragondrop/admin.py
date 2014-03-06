from django.contrib import admin
from dragondrop.models import Folder, Bookmark, BinFolder, BookmarkToFolder
from django.contrib.auth.models import User

admin.site.register(Folder)
admin.site.register(Bookmark)
admin.site.register(BinFolder)
admin.site.register(BookmarkToFolder)

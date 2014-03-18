Dragon-Drop
===========

A bookmarking site which will change the way you search.

Deployed to dragondrop.pythonanywhere.com


Test:
Username: Leif
Password: Leifpassword

If you would like to see a user account with folders/bookmarks already present (test data)

Username: Jean
Password: Jeanpassword


Cloning this repo should give direct access to DragonDrop when the server is run, as dragondrop.db is present in the folder.

If not, syncdb, and run populate_dragondrop.py. 

The site itself has some help on each screen, but an overview of help follows:

1) Add folders using the link in the left hand column.
2) Search, and if you like a bookmark, drag it into the folder.
3) If you do not like a bookmark, you can drag it into the bin folder and never see it again.
4) Your 5 most recent bookmarks, and the 5 top bookmarks of the site are displayed on the right.
5) Clicking on a folder brings you into the folder page.
6) You can rank the bookmarks, delete them, tweet them, and manually add them.
7) Ranking the bookmarks impacts the output of searching.


Also included in this repository are

1) requirements.txt - the pip requirements file
2) Updated presentation, with checklist of implemented functionality.

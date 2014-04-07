import csv
import re
import random

addUserSet = set()
addFolderSet = set()
addBookmarkSet = set()
addBookmarkToFolderSet = set()
addBinFolderSet = set()

with open('links3.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i,row in enumerate(csvreader):
        addUserSet.add( "\t" + row[0] + " = User.objects.create_user('" + row[0] + "',None, '" + row[0] + "password')" + "\n\t" + row[0] + ".save()" )
        addFolderSet.add("\tf_" + row[1].replace(" ","_") + "_" + row[0] + " = add_folder(foldername='" + row[1] + "',fusername_fk=" + row[0] + ")")
        addBookmarkSet.add("\tbmID_" + str(i) + ",bmID_b_" + str(i) + " = Bookmark.objects.get_or_create(url='" + row[2] + "')\n" + "\tbmID_" + str(i) + ".btitle='" + re.sub(r'[^\w]', ' ', row[3]) + "'\n\tbmID_" + str(i) + ".bdescr='" + re.sub(r'[^\w]', ' ', row[3]) + "'\n\tbmID_" + str(i) + ".save()" + "\n\tbfID_" + str(i) + " = "+  "BookmarkToFolder.objects.create(bffolder=f_" + row[1].replace(" ","_") + "_" + row[0] + ",bfbookmark=bmID_" + str(i) + ",bfrank=" + str(random.random()) + ",clicks=" + str(random.randint(0,100)) + ")" + "\n\tbfID_" + str(i) + ".save()" ) #\n\tbmID_" + str(i) + ".fname.add(" + "bfID_" + str(i) + ")")
        addBinFolderSet.add(row[0])
        
    print "import os"
    print "import dragondrop.get_domain_from_url"
    print "\ndef populate():\n"
    
    print "\t#Users" 
    for user in addUserSet:
        print user    
    print "\tLeif = User.objects.create_user('Leif',None, 'Leifpassword')" + "\n\t" + row[0] + ".save()"
        
    print "\n\t#Folders"    
    for entry in addFolderSet:
        print entry
        
    print "\n\t#Bookmarks"
    for entry in addBookmarkSet:
        print entry

    print "\n\t#Bin Folders"
    for i, entry in enumerate(addBinFolderSet):
        print "\tbinID_" + str(i) + " = add_binfolder(busername_fk=" + entry + ")"
    
print "\ndef add_bookmark(url, btitle, bdescr, bdomain, fname, saved_times=0):\n" + "\tbm = Bookmark.objects.get_or_create(url=url, btitle=btitle, bdescr=bdescr, bdomain=bdomain, fname=fname, saved_times=saved_times)[0]\n" + "\treturn bm"
print "\ndef add_folder(foldername, fusername_fk):\n" + "\tf = Folder.objects.get_or_create(foldername=foldername, fusername_fk=fusername_fk)[0]\n" + "\treturn f"
print "\ndef add_binfolder(busername_fk):\n" + "\tbf = BinFolder.objects.get_or_create(busername_fk=busername_fk)[0]\n\treturn bf"

print "\n# Start execution here!\n" + "if __name__ == '__main__':\n" + "\tprint 'Starting DragonDrop population script...'\n" + "\tos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dragondrop_proj.settings')\n" + "\tfrom dragondrop.models import User, Bookmark, Folder, BinFolder, BookmarkToFolder \n" + "\tpopulate()"
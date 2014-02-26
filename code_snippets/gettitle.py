import urllib2
import re


url = "http://stackoverflow.com/questions/19944506/java-incrementing-a-variable-inside-of-a-for-loop"

def getHtmlTitle(url):
    req = urllib2.Request(url)

    # Try to read only the first 65,536 bytes
    req.headers['Range']='bytes=%s-%s' % (0,65535)
    
    try:
        f = urllib2.urlopen(req)

        # Assign the first 65,536 bytes to the variable html
        html = f.read(65536)

    except (urllib2.URLError, urllib2.HTTPError) as e:
        return "--- Page not retrieved ---"

    # Look for the title tag
    titlePattern = re.compile("<title[^>]*>(.*?)</title>")
    titleResult = titlePattern.search(html)
    if titleResult:
        title = titleResult.group(1)
    else:
        title = "--- Title not found ---"


    descriptionTagPattern = re.compile("<meta[^>]*name=\"description\"[^>]*>")
    descriptionTagResult = descriptionTagPattern.search(html)
    if descriptionTagResult:
        descriptionTag = descriptionTagResult.group(0)
        descriptionPattern = re.compile("content=\"(.*?)\"")
        descriptionResult = descriptionPattern.search(descriptionTag)
        if descriptionResult:
            description = descriptionResult.group(1)
        else:
            description = "--- Description not found ---"
    else:
        description = "--- Description not found ---"
        
    return (title, description)
        

        
print getHtmlTitle("http://bing.com")
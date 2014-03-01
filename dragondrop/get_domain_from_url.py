from urlparse import urlparse

# Given a URL (e.g. http://www.bing.com/images), this function returns the domain
# (e.g. bing.com). It's could probably be improved but hopefully works reasonably well.
def getDomain(url):
    domain = urlparse(url).netloc
    domain_parts = domain.split('.')
    if domain_parts[0] == "www":
        return '.'.join(domain_parts[1:])
    else:
        return domain
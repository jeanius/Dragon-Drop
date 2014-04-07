import re
from django.db.models import Q
from dragondrop.models import Bookmark
import operator

"""
methods
    normalize_query(), get_query()

    adapted from:
    http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap

"""

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(query_string):
    """
    this function searches the bookmarks model's title and description for the given
    query_string
    it returns the top three folders in which the bookmarks contain the query_string

    functions used: get_query
    """

    found_entries = None

    entry_query = get_query(query_string, ['btitle', 'bdescr',])

    found_entries = Bookmark.objects.filter(entry_query).order_by('-saved_times')

    context_dict = {}

    for result in found_entries:
        for folder_res in result.fname.all():
            if folder_res in context_dict:
                context_dict[folder_res] += 1
            else:
                context_dict[folder_res] = 1

    sorted_dict = sorted(context_dict.iteritems(), key=operator.itemgetter(1))[::-1]

    top_three = [i[0] for i in sorted_dict][:3]

    return top_three
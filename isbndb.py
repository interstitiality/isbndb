"""Python2 wrapper for ISBNDB.com API

This is meant to be a simple script to utilize the ISBNDB.com 
database.

In future versions, this should provide the option of using any of the 
three return formats that ISBNDB.com offers - json, yaml, xml - 
but for now it has limited capability, due to the scope of the project
for which it was originally written.

Written by Lucas Smith (ashenphoenix@sdf.org), Copyleft.
If you think it needs some work, tell him.  Or write it in.
Or if you would like to help:

TODO
- add operability for xml and json
- switch Pull return from array/dictionary to more objecty output
- include wider info range in fields variable of Cull
- use it in a project and share the results

"""

import urllib, yaml

returnFormat = 'yaml' 

key = #enter key here: you have to create an account with isbndb.com to get one of these 

def Pull(isbn=9780679428510):
    """pulls book information from ISBNDB"""
    isbn = str(isbn)
    url = "http://www.isbndb.com/api/v2/%s/%s/book/" % (returnFormat, key) + isbn
    raw_info = urllib.urlopen(url)
    book_info = yaml.load(raw_info.read())['data'][0]
    return book_info

def Cull(array):
    """culls relevant information from Pull"""
    book_info = {}
    fields = ['edition_info', 'isbn13', 'publisher_name', 'summary', 'title', 'author_data', 'subject_ids']
    for bit in fields:
        if array[bit] and not array[bit] == []:
            if bit == 'author_data':
                authorList = []
                for index in range(len(array[bit])):
                    authorList.append(array[bit][index]['name'])
                book_info[bit] = authorList
            else:
                book_info[bit] = array[bit]
    return book_info

__all__ = ['Pull', 'Cull', 'returnFormat', 'key']

# Uncomment the following lines to make this callable from the CLI
#
#entry = Pull(raw_input("What is the ISBN of the book that you would like to look up? "))
#print Cull(entry)

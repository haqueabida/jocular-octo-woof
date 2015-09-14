# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:02:05 2015

@author: ahaque
"""

# y = a list of search logs
 
 
from search_popularity import *


all_search_terms = []
all_search_phrases = []

for files in y:
    filename = "search/"+files
    (search_terms, search_phrases) = create_search(filename)
    all_search_terms.append(search_terms)
    all_search_phrases.append(search_phrases)
    
flat_search = [item for sublist in all_search_terms for item in sublist]

print freq_dict(flat_search)
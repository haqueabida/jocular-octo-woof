# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:58:32 2015

@author: ahaque
"""

import json           

def create_search(filename):
    data = []
    search_terms = []        
    search_phrases = []
    with open(filename) as f:
        for line in f:
            if line[0:10]=='{"params":':
                data.append(json.loads(line))

#    
    for d in data:
        single_search = []
        y = d["params"]
        for i in y:
            j = str(i["term"])
            single_search.append(j)
            search_terms.append(j)
            
        if len(single_search)>1:
            search_phrases.append(",".join(single_search))
    
        
    return search_terms, search_phrases

def num_search(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            if line[0:10]=='{"params":':
                count+=1
    return count     
#(search_terms, search_phrases) =create_search('search.json')

"""
Bit of a hack: search_phrases does the phrases (people have searched with multiple tags)
search_terms splits them all up into singletons. So for example if the search for "cats, dogs" and "dogs"
are done as separate searches then "dog" has been searched twice (added to search_terms twice).
However, "dogs" does not get added to search_phrases, as it is a singleton. It only gets added to
search_terms. "cats, dogs" gets added to search_phrases.

Second hack: Since you can't key by lists (lists are mutable), I just turned the phrase into a string
and keyed by that.
"""
#
#
def freq_dict(phrases):
    words = [str(s) for s in phrases] 
    d = {w: 0 for w in words}
    for word in words:
        d[word] += 1
        
    return d
"""
returns the top perc% of the list, if you just want top searches.

"""
def top_percent(fd, perc):
    import numpy as np
    p = np.percentile(fd.values(), 100-perc)
    
    top_dict = {}
    
    for i in fd:
        if fd[i]>=p:
            top_dict[i] = fd[i]
            
    return top_dict
    

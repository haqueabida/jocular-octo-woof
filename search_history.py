# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:02:05 2015

@author: ahaque
"""

import os
from os import path

# y = a list of search logs
dir_path = "C:\\Users\\ahaque\\Documents\\aws_attempt\\production\\SearchLogs"
files = [x for x in os.listdir(dir_path) if path.isfile(dir_path+os.sep+x)]

last_week = [x for x in files if x>="searchLog-2015-09-07"]

from search_popularity import *


all_search_terms = []
all_search_phrases = []

for files in last_week:
    all_count = 0
    filename = dir_path+"\\"+files
    (search_terms, search_phrases) = create_search(filename)
    all_search_terms.append(search_terms)
    all_search_phrases.append(search_phrases)
    all_count+=num_search(files)
    
flat_search = [item for sublist in all_search_terms for item in sublist]

print freq_dict(flat_search)
import json
import os
import requests 


CACHE_NAME = "nutrition_cache.json"

try:
    cache_file = open(CACHE_NAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def fetch_from_cache(identifier):
    pass

def add_to_cache(identifier):

    pass


    
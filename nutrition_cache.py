import json
import os
import requests 
import nutritionix



CACHE_NAME = "nutrition_cache.json"

try:
    cache_file = open(CACHE_NAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def fetch_from_cache(identifier):
    if drink:
        drink = CACHE_NAME.nutritionix.get_drink()
        return drink
    else:
        return None

def add_to_cache(identifier):
    CACHE_DICTION[unique_ident] = json.loads(resp.text)
    dumpted_json_cache = json.dumps(CACHE_DICTION, indent=2)
    fw = open(CACHE_NAME, 'w')
    fw.write(dumped_json_cache)
    fw.close()
    pprint(CACHE_DICTION[unique_ident])
    return CACHE_DICTION[unique_ident]

    
import requests
import os 
from pprint import pprint
import logging
import nutrition_cache
import time

cached_time = 300

key = os.environ.get('DRINK_KEY')
id = os.environ.get('DRINK_ID')

url = f'https://api.nutritionix.com/v2/search'

#def params_unique_conbination(baseurl, params, private_key=key, private_id=id):
    #alphabetized_keys = sorted(params_d.keys{})
    #res = []
    #for k in alphabetized_keys:
        #if k not in private_keys:
            #res.append("{}".format(k, params_d[k]))
    #return baseurl + "_",join()



#
def get_drink(search_term):
    
    try:
        query = {'q': search_term, 'limit': '1', 'offset': '0' , 'appId': id, 'appKey': key }
        data = nutritionix_api_call(query)
        results = data['results']
        try:
            results = mydict['results']
        except:
            results = default_results
        

        if results:
            result = results [0]
            beverage = result['item_name']
            return beverage
        else:
            print('Sorry, Product not found in the database. Please Try Again.')
            return None
            
            
    except Exception as e:
        logging.exception(f'Error occured while calling the Nutritionix API. {e} ')

    except KeyError as e:
        print(f"Key {results}not found")
        
    


def nutritionix_api_call(query):
    return requests.get(url, params=query).json()
    now = time.time()




    #try:
        
        #results = data['results']

        #for result in results:
           # drink_name = result['item_name']
        #return drink_name

    #except Exception as e:
        #print('Error with your query. ')





#url = f'https://api.nutritionix.com/v2/search?{search_drink}&limit=1&offset=0&appId={id}&appKey={key}'
#q={search_drink}&limit=1&offset=0&appId={id}&appKey={key}
# https://api.nutritionix.com/v2/search?q=mango&limit=2&offset=0&appId=b3203af1&appKey=2b9b96bfe1278528cc9717ce7055a037

import requests
import os 
from pprint import pprint

app_key = os.environ.get('DRINK_KEY')
app_id = os.environ.get('DRINK_ID')


def get_drink(search_term):
    
    url = f'https://api.nutritionix.com/v2/search?q={search_term}&limit=1&offset=0&appId={app_id}&appKey={app_key}'
    try:
        data = requests.get(url).json()
        results = data['results']

        for result in results:
            drink_name = result['item_name']
        return drink_name

    except Exception as e:
        print('Error with your query. ')

#url = f'https://api.nutritionix.com/v2/search?{search_drink}&limit=1&offset=0&appId={id}&appKey={key}'
#q={search_drink}&limit=1&offset=0&appId={id}&appKey={key}
# https://api.nutritionix.com/v2/search?q=mango&limit=2&offset=0&appId=b3203af1&appKey=2b9b96bfe1278528cc9717ce7055a037




import nutritionix
import unittest
from unittest import TestCase
from unittest.mock import patch

class testAPI(TestCase):

     # option 1 - happy path - at least one recipe returned 
    # mock the API call
    @patch('nutritionix.nutritionix_api_call', return_value={'results': "item_name"})  # replace with example response in the same structure the API uses
    def test_api_returns_data_if_data_exists(self, mock_api_call):
        
        # if it's easier you can set the side effect here instead of in the @patch decorator
        mock_api_call.return_value = {"item_name": "Pepsi"} # whatever it is 
        drink = nutritionix.get_drink( "Pepsi")

        self.assertIsNone(drink, "Pepsi" )
        # assert title is the title from the example response data
        # assert url is the url from the example response 


        # option 2 - ok path - no data - searching for something like "235645630349u90354u39045u" that there are no recipes for 
    # results is empty list  
    # change the method name :)

    @patch('nutritionix.nutritionix_api_call', return_value= '1651')  # fill in example no data response in the same format the API uses
    def test_api_does_whatever_it_does_when_no_results(self, mock_api_call):
        example_return = '1651'
        example_api_respose = {'q': example_return, 'limit': '1', 'offset': '0' , 'appId': id }
        example_return = ['example_api_response']
        drink = nutritionix.get_drink('search_term' )
        self.assertNotEqual(drink, '1651')
        #assert that the get_recipe method correctly returns a response that indicates no value 


    # option 3 - unhappy path - call is made, response recived but it is an error message 
    # # many APIs return a JSON response e.g. { "error": "missing API key" }
    # what if JSON is not in expected format? 
    #@patch('nutritionix.nitritionix_api_call', return_value={"error": "missing API key" })  # fill in example no error JSON data response in the same format the API uses
    #def test_api_call_handles_error_responses_from_api(self, mock_api_call):
        # what does the API do when you make a request it doesn't understand, e.g. key invalid?
        # many APIs return a JSON response e.g. { "error": "missing API key"}
        # what should you app do?
        #recipe = nutritionix.get_drink('not a food')
        #self.assertEqual(recipe, 'Pepsi')
        # assert that the get_recipe method correctly returns a response that indicates no value 


# option 4 - unhappy path - error connecting - API server down, no internet ... 
    # change the method name :)
    @patch('nutritionix.nutritionix_api_call', side_effect=Exception('Error occured while calling the Nutritionix API. ' ))  #  spoonacular_api_call will raise an exception if connection error 
    def test_api_does_whatever_it_does_when_error_connecting(self, mock_request_get):
        drink = nutritionix.get_drink('Sweetened Green Tea')
        self.assertFalse(drink, 'Error occured while calling the Nutritionix API. ')
        

        # assert that the get_recipe method behave correctly if connection error 
        # maybe it returns a message, maybe it raises an exception ? 



if __name__ == '__main__':
   unittest.main()
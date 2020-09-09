#
import requests_with_caching
#q= search query
#limit = max no. of reccomendations
def get_movies_from_tastedive (movie):
    baseurl = "https://tastedive.com/api/similar"
    param_dict = {}
    param_dict['q'] = movie
    param_dict['type'] = "movies"
    param_dict['limit'] = 5
    
    tastedive_resp = requests_with_caching.get(baseurl, params = param_dict, )
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

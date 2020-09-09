import requests_with_caching
import json

#input = movie title
#output = dict with info about movie
def get_movie_data(movie_title):
    baseurl = "http://www.omdbapi.com/"
    param_dict = {}
    param_dict["t"] = movie_title
    param_dict["r"] = "json"
    
    omdb_resp = requests_with_caching.get(baseurl,params = param_dict)
    return omdb_resp.json()

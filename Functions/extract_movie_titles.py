import requests_with_caching
import json
#q= search query
#limit = max no. of reccomendations
def get_movies_from_tastedive (movie):
    baseurl = "https://tastedive.com/api/similar"
    param_dict = {}
    param_dict["q"] = movie
    param_dict["type"] = "movies"
    param_dict["limit"] = 5
    
    tastedive_resp = requests_with_caching.get(baseurl, params =param_dict)
    print(tastedive_resp.json())
    return tastedive_resp.json()

def extract_movie_titles(movie_dict):
    #print(movie_dict)
    extracted_results = []
    for x in movie_dict['Similar']['Results']:
        #print (x['Name'])
        name = x['Name']
        extracted_results.append(name)
    return extracted_results

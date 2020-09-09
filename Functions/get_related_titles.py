
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
    #print(tastedive_resp.json())
    return tastedive_resp.json()

def extract_movie_titles(movie_dict):
    #print(movie_dict)
    extracted_results = []
    for x in movie_dict['Similar']['Results']:
        #print (x['Name'])
        name = x['Name']
        extracted_results.append(name)
    return extracted_results

#input = list of movie titles
def get_related_titles(movie_title_list):
    #For each movie in the list, get 5 related movies
    resulting_list = []
    for movie in movie_title_list:
        extracted_list = extract_movie_titles(get_movies_from_tastedive(movie))
        for title in extracted_list:
            if title not in resulting_list:
                resulting_list.append(title)
    return resulting_list  

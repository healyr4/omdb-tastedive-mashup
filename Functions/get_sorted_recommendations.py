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




#input = movie title
#output = dict with info about movie
def get_movie_data(movie_title):
    baseurl = "http://www.omdbapi.com/"
    param_dict = {}
    param_dict["t"] = movie_title
    param_dict["r"] = "json"
    
    omdb_resp = requests_with_caching.get(baseurl,params = param_dict)
    #print (omdb_resp.json())
    return omdb_resp.json()

#Extract rotten tomatoes movie rating
#Input = movie info
#Output = rating
def get_movie_rating(movie_info):
    rating_str = ""
    print(movie_info)
    for x in movie_info["Ratings"]:
        #print(x["Source"])
        if x["Source"] == "Rotten Tomatoes":
            rating_str = x["Value"]
        #If there is no rating return 0
        if rating_str != "":
                #[:2] to remove "%"
                rating = rating_str[:2]
                rating = int(rating)
        else:
            rating = 0
    return rating

#input - list of movie titles
#output = sorted list of related movies
#Descending order by Rotten Tomatoes rating
#Ties broken in reverse alphabetical order
def get_sorted_recommendations(movie_titles_list):
    related_list = get_related_titles(movie_titles_list)
    ranked_list = sorted(related_list, key = lambda movie: (get_movie_rating(get_movie_data(movie)), movie), reverse=True)
    return ranked_list
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


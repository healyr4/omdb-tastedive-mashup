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
        
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

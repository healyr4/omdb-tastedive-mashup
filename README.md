# Python Data Collection and Processing Course Project
This is the final project of the Data Collection and Processing Course with Python. This course is part of a 5 course collection from the University of Michigan on Coursera. More in formation can be found [here](https://www.coursera.org/learn/data-collection-processing-python/home/welcome)

# Description
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

TasteDive provides recommendations of similar music, movies, TV shows etc. based on what you search for.

The OMDb API is a RESTful web service to obtain movie information


# Material
TasteDive Api Documentation: https://tastedive.com/read/api

OMDB Api Documentation: https://www.omdbapi.com/

# Functions
(1) **get_movies_from_tastedive(string)**:
Takes input parameter, a string that is the name of a movie or music artist. Returns the 5 TasteDive results that are associated with that string. Only gets movies, not other kinds of media. It returns a python dictionary with just one key, ‘Similar’.

(2) **get_movies_from_tastedive(dict):**
Extracts just the list of movie titles from a dictionary 

(3) **get_related_titles(movie_title_list):**
Gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. The same movies aren't included twice.

(4) **get_movie_data (movie_title):**
Takes a string that represents the title of a movie you want to search. The function returns a dictionary with information about that movie from OMDB

(5) **get_movie_rating (movie):**
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating it returns 0.

(6) **get_sorted_recommendations (movie_titles_list):**
It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies are sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Ties are broken in reverse alphabetic order, so that ‘Yahşi Batı’ for example, comes before ‘Eyyvah Eyvah’.


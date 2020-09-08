# Python Data Collection and Processing Course Project
This is the final project of the Data Collection and Processing Course with Python. This course is part of a 5 course collection from the University of Michigan on Coursera. More in formation can be found [here](https://www.coursera.org/learn/data-collection-processing-python/home/welcome)

# Description
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

# Material
TasteDive Api Documentation: https://tastedive.com/read/api

OMDB Api Documentation: https://www.omdbapi.com/

# Functions
(1) get_movies_from_tastedive(string):
Takes input parameter, a string that is the name of a movie or music artist. Returns the 5 TasteDive results that are associated with that string. Only gets movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

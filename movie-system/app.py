import json
import os

from user import User


def menu():
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                       ", 'f' to save or 'q' to quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                           "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                           ", 'f' to save or 'q' to quit")


def file_exists(filename):
    return os.path.isfile(filename)


menu()


"""
with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())
"""


#user = User("Mustafa")

#user.add_movie("The Matrix", "Sci-Fi")
#user.add_movie("The Interview", "Comedy")

"""
with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)
"""

#print(user.json())

#user.add_movie("The Matrix", "Sci-Fi")
#user.add_movie("Iron Man", "Sci-Fi")

#user = user.load_from_file('Mustafa.txt')

#user.save_to_file()

#print(user.name)
#print(user.movies)


#my_movie = Movie("The Matrix", "Sci-Fi", True)
#user.movies.append(my_movie)
#print(user)     # <--- repr will resolve the issue of return memory location
#print(user.name)
#print(user.movies)
#print(user.watched_movies())

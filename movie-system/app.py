from user import User

user = User("Mustafa")

#user.add_movie("The Matrix", "Sci-Fi")
#user.add_movie("Iron Man", "Sci-Fi")

user = user.load_from_file('Mustafa.txt')

#user.save_to_file()

print(user.name)
print(user.movies)


#my_movie = Movie("The Matrix", "Sci-Fi", True)
#user.movies.append(my_movie)
#print(user)     # <--- repr will resolve the issue of return memory location
#print(user.name)
#print(user.movies)
#print(user.watched_movies())

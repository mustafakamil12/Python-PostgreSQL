from movie import Movie
from user import User

user = User("Mustafa")

my_movie = Movie("The Matrix", "Sci-Fi", False)

user.movies.append(my_movie)

#print(user)     # <--- repr will resolve the issue of return memory location
#print(user.name)
#print(user.movies)
print(user.watched_movies())

movies = ['The Matrix', 'Enemy at the gates', 'Iron Man']

def checkMovies(name,movies):
	movies = list(filter(lambda movie: movie != name, movies))
	print(movies)

checkMovies('Iron Man',movies)
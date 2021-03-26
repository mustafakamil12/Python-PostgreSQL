from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):     # This function used if u try to print the object only.
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        """
        watched_movies_list = []

        for movie in self.movies:
            if movie.watched:
                watched_movies_list.append(movie)
        return watched_movies_list
        """
        return list(filter(lambda movie: movie.watched, self.movies))
    """ csv from the last century...
    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, movie.watched))

    # Because we didn't need to use self in the method below we are going to use:
    @classmethod
    def load_from_file(cls, filename):      # where cls stand for User <class name>
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")    # ['name', 'genre', 'watched']
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = cls(username)
            user.movies = movies
            return user
    """
    



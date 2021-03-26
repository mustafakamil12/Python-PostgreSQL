class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)

    def json(self):
        return{
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):  # {'genre': '...', 'name': '....', 'watched': True}
        #return Movie(json_data['name'], json_data['genre'], json_data['watched'])

        # if we need to be more explicit about what we pass and ensure
        #return Movie(genre=json_data['genre'], watched= json_data['watched'], name= json_data['name'])

        # to pass dictionary as set of name parameters
        return Movie(**json_data)



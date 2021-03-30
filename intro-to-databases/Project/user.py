# import psycopg2
from database import CursorFromConnectionFromPool


# from database import connect

# self is currently bounded object
# cls is currently bounded class
# using connect() just to explain how we can avoid doublication in the code.
# it's not practically to open connection and close it all over the application
# it's better to create connection pool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    """
    old approach
    def save_to_db(self):
        connection = psycopg2.connect(database="learning", user="mustafaalogaidi",
                                      password="Pit5cxcy", host="localhost")
        with connection.cursor() as cursor:
            cursor.execute('insert into users(email,first_name,last_name) values(%s,%s,%s)',
                           (self.email, self.first_name, self.last_name))
        connection.commit()
        connection.close()
    """

    """
    we will use a new approach called connection pool
    def save_to_db(self):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('insert into users(email,first_name,last_name) values(%s,%s,%s)',
                               (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        # to create another object withing class
        # another_user = cls('rolf@gmail.com", "Rolf", "Smith", None)
        # where cls is exactly like using User in the app
        with psycopg2.connect(database="learning", user="mustafaalogaidi",
                              password="Pit5cxcy", host="localhost") as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from users where users.email = %s', (email,))  # here the email is inside tuple
                user_data = cursor.fetchone() # this function is retrieve only one
                # return new object :)
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=
                           user_data[0])
    """

    def save_to_db(self):
        # connection = connection_pool.getconn()
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('insert into users(email,first_name,last_name) values(%s,%s,%s)',
                           (self.email, self.first_name, self.last_name))
        # connection_pool.putconn(connection)     This line is to return connection to the pool

    @classmethod
    def load_from_db_by_email(cls, email):
        # to create another object withing class
        # another_user = cls('rolf@gmail.com", "Rolf", "Smith", None)
        # where cls is exactly like using User in the app
        # connection = connection_pool.getconn()
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select * from users where users.email = %s', (email,))  # here the email is inside tuple
            user_data = cursor.fetchone()  # this function is retrieve only one
            # return new object :)
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])








from user import User
from database import Database

"""
print(Database.connection_pool)
Database.initialise()
print(Database.connection_pool)
"""

my_user = User("Muhanned.alogaidi@icloud.com", "Muhanned", "Al Ogaidi", None)

Database.initialise()

my_user.save_to_db()
#print(my_user.email)
#print(my_user)

what_we_got = User.load_from_db_by_email('mena.alogaidi@icloud.com')    # Notice we use class name User
print(what_we_got.email, what_we_got.first_name, what_we_got.last_name, what_we_got.id)

my_user = User("Ahmed.alogaidi@icloud.com", "Ahmed", "Al Ogaidi", None)
my_user.save_to_db()


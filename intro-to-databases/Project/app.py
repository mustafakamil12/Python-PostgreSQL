from user import User
from database import Database

"""
print(Database.connection_pool)
Database.initialise()
print(Database.connection_pool)
"""

#my_user = User("Mayam.alogaidi@icloud.com", "Maryam", "Munnes", None)

Database.initialise(database="learning", user="mustafaalogaidi", password="Pit5cxcy", host="localhost")

#my_user.save_to_db()
#print(my_user.email)
#print(my_user)

what_we_got = User.load_from_db_by_email('mena.alogaidi@icloud.com')    # Notice we use class name User
print(what_we_got.email, what_we_got.first_name, what_we_got.last_name, what_we_got.id)

#my_user = User("Hala.Jamal@icloud.com", "Hala", "Jamal", None)
#my_user.save_to_db()


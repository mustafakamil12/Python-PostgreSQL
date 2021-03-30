import psycopg2

connection = psycopg2.connect(database="learning", user="mustafaalogaidi", password="Pit5cxcy", host="localhost")

cursor = connection.cursor()
cursor.execute('select * from users')

for row in cursor:
	print(row)

#connection.commit()
#connection.close()


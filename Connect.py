import sqlite3

db = sqlite3.connect("user_database.db")

cursor = db.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS
#user(user_id INTEGER PRIMARY KEY,user_name TEXT)""")

#cursor.execute("""INSERT INTO user VALUES (00001, 'IJAM')""")

#cursor.execute("""DELETE FROM user""")

print(cursor.fetchall())

db.commit()
db.close()
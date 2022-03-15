import sqlite3
from cypter import *
from datetime import datetime
from random import randint
    
db = sqlite3.connect("user_database.db")
cursor = db.cursor()
date = str(datetime.now()).split(" ")[0].replace("-","_")

def list_column():
    column_name = []
    for i in cursor.execute("""PRAGMA table_info(user)"""):
        column_name.append(i[1])
    return column_name

def add_data(changed_par_col, search_col, value, recent):
    cursor.execute(f"""UPDATE user SET '{changed_par_col}' = '{value}' WHERE {search_col} = '{recent}'""")

def new_column(col_name):
    cursor.execute(f"""ALTER TABLE user ADD COLUMN '{col_name}'""")

def generate_id():
    randnum = str(randint(0,10000000))
    result = randnum
    if len(randnum) != 7:
        for i in range(7-len(randnum)):
            result= "0"+result
    return result

def add_user(id, username):
    cursor.execute(f"""INSERT INTO user (user_id, user_name) VALUES ({id}, '{username}')""")

def precence(id):
    add_data(date, 'user_id', 'attend', id)
#cursor.execute("""CREATE TABLE IF NOT EXISTS
#user(user_id INTEGER PRIMARY KEY,user_name TEXT)""")
#cursor.execute("""INSERT INTO user VALUES (00001, 'IJAM')""")
#x = cursor.execute("""SELECT * FROM user WHERE user_name = 'adit'""")
#print(cursor.fetchone())
#cursor.execute("""DELETE FROM user""")
#cursor.execute("""ALTER TABLE user DROP COLUMN location""")

def commit():
    db.commit()
    db.close()
import sqlite3
from cypter import *
from datetime import datetime
from random import randint

class Database():
    def __init__(self, filename):
        self.db = sqlite3.connect(filename)
        self.cursor = self.db.cursor()
        self.date = str(datetime.now()).split(" ")[0].replace("-","_")

    def list_column(self):
        column_name = []
        for i in self.cursor.execute("""PRAGMA table_info(user)"""):
            column_name.append(i[1])
        return column_name

    def add_data(self, changed_par_col, search_col, value, recent):
        self.cursor.execute(f"""UPDATE user SET '{changed_par_col}' = '{value}' WHERE {search_col} = '{recent}'""")

    def new_column(self, col_name):
        self.cursor.execute(f"""ALTER TABLE user ADD COLUMN '{col_name}'""")

    def generate_id(self):
        randnum = str(randint(0,10000000))
        result = randnum
        if len(randnum) != 7:
            for i in range(7-len(randnum)):
                result= "0"+result
        return result

    def add_user(self, id, username):
        self.cursor.execute(f"""INSERT INTO user (user_id, user_name) VALUES ({id}, '{username}')""")

    def precence(self, id):
        self.add_data(self.date, 'user_id', 'attend', id)
    #cursor.execute("""CREATE TABLE IF NOT EXISTS
    #user(user_id INTEGER PRIMARY KEY,user_name TEXT)""")
    #cursor.execute("""INSERT INTO user VALUES (00001, 'IJAM')""")
    #x = cursor.execute("""SELECT * FROM user WHERE user_name = 'adit'""")
    #print(cursor.fetchone())
    #cursor.execute("""DELETE FROM user""")
    #cursor.execute("""ALTER TABLE user DROP COLUMN location""")

    def commit(self):
        self.db.commit()
        self.db.close()
    
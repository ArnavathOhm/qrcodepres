from random import randint
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Database:
    def __init__(self, url):
        self.db = create_engine(url)
        self.session = Session(self.db)

    def list_column(self):
        column_name = []
        for i in self.session.execute("""PRAGMA table_info(user)"""):
            column_name.append(i[1])
        return column_name

    def update(self, changed_par_col, search_col, value, recent):
        self.session.execute(
            f"""UPDATE user SET '{changed_par_col}' = '{value}' WHERE {search_col} = '{recent}'"""
        )

    def new_column(self, col_name):
        self.session.execute(f"""ALTER TABLE user ADD COLUMN '{col_name}'""")

    def generate_id(self):
        randnum = str(randint(0, 10000000))
        while self.select_user(randnum):
            randnum = str(randint(0, 10000000))
        return randnum.zfill(7)

    def add_user(self, id, username):
        self.session.execute(
            f"""INSERT INTO user (user_id, user_name) VALUES ({id}, '{username}')"""
        )

    def precence(self, id, date):
        self.update(date, "user_id", "attend", id)

    # cursor.execute("""CREATE TABLE IF NOT EXISTS
    # user(user_id INTEGER PRIMARY KEY,user_name TEXT)""")
    # cursor.execute("""INSERT INTO user VALUES (00001, 'IJAM')""")
    # x = cursor.execute("""SELECT * FROM user WHERE user_name = 'adit'""")
    # print(cursor.fetchone())
    # cursor.execute("""DELETE FROM user""")
    # cursor.execute("""ALTER TABLE user DROP COLUMN location""")

    def select_user(self, id):
        return self.session.execute(
            f"""SELECT * FROM user WHERE user_id = '{id}'"""
        ).all()

    def create(self):
        self.session.execute(
            """
        CREATE TABLE IF NOT EXISTS
        user(user_id INTEGER PRIMARY KEY, user_name TEXT)
        """
        )

    def delete_all(self):
        self.session.execute(
            """
        DELETE FROM user
        """
        )

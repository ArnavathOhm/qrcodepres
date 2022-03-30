from dotenv import load_dotenv
import os

load_dotenv(".env")
basedir = os.path.abspath(os.path.dirname(__file__))


class Production:
    TESTING = False
    DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "user_database.db"
    )

    if "postgres:" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("postgres:", "postgresql:")


class Testing:
    TESTING = True
    DATABASE_URL = "sqlite:///" + os.path.join(basedir, "test.db")

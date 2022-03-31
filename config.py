from dotenv import load_dotenv
import os

load_dotenv(".env")
basedir = os.path.abspath(os.path.dirname(__file__))


class Production:
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dn98738ynid0qna948hAFahw"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "user_database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "cerulean"

    if "postgres:" in SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres:", "postgresql:"
        )


class Testing(Production):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


def get_key():
    return os.environ.get("KEY_COMPILER").encode("utf-8")


def encriptIT(text):
    return Fernet(get_key()).encrypt(text.encode("utf-8"))


def decryptIT(text):
    try:
        return Fernet(get_key()).decrypt(text.encode("utf-8")).decode("utf-8")
    except:
        return None


if __name__ == "__main__":
    print(encriptIT("1").decode("utf-8"))

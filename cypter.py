from cryptography.fernet import Fernet

def get_key(filename = "Key_Compiler.txt"):
    with open(filename,"r") as file:
        return file.read().encode("utf-8")

def encriptIT(text):
    return Fernet(get_key()).encrypt(text.encode("utf-8"))

def decryptIT(text):
    return Fernet(get_key()).decrypt(text).decode("utf-8")

def acc_ip(filename = "Accesable_IP.txt"):
    with open(filename,"r") as file:
        return file.read().split(",")


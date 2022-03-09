from sys import dont_write_bytecode
from turtle import done
from flask import *
from test import *

app = Flask(__name__)

@app.route('/')
def landingpage():
    accesible = acc_ip()
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = (request.environ['REMOTE_ADDR'])
    else:
        ip = (request.environ['HTTP_X_FORWARDED_FOR'])

    if ip in accesible:
        return "done"
    else:
        return "Not a Admin"
    

if __name__ == "__main__":
    app.run(debug=True)
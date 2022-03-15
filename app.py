from sys import dont_write_bytecode
from db_connect import Database
from flask import *
from test import *
from datetime import datetime

date = str(datetime.now()).split(" ")[0].replace("-","_")

app = Flask(__name__)

def acc_ip():
    with open("Accesable_IP.txt",'r') as fl:
        accesible = fl.read().split(",")
    return accesible

@app.route('/')
def landingpage():
    accesible = acc_ip()
    connect = Database('user_database.db')
    passwr = request.args.get('ert426ip')

    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = (request.environ['REMOTE_ADDR'])
    else:
        ip = (request.environ['HTTP_X_FORWARDED_FOR'])

    if passwr == "uywoaNdqoap12Jd01djls" and ip not in accesible:
        with open("Accesable_IP.txt","a")as fl:
            fl.write(f",{ip}")

    if ip in accesible:
        id = request.args.get('id')
        if id == None:
            return render_template("Bad-Format.html")
        if date in connect.list_column():
            try:
                connect.precence(id)
                connect.commit()
                return render_template("200-OK.html")
            except:
                return 'invalid user'
        else:
            connect.new_column(date)
            connect.commit()
    else:
        return render_template("403-Forbidden.html")
    
if __name__ == "__main__":
    app.run(debug=True)
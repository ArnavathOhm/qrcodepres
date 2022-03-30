from db_connect import Database
from flask import Flask, request, jsonify
from datetime import datetime
from os import path
from config import Production
import cypter

basedir = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Production)


def acc_ip():
    with open(path.join(basedir, "Accesable_IP.txt"), "r") as fl:
        accesible = fl.read().split(",")
    return accesible


@app.route("/")
def index():
    date = str(datetime.now()).split(" ")[0].replace("-", "_")
    connect = Database(app.config["DATABASE_URL"])

    # Securing api with ip address
    passwr = request.args.get("ert426ip")
    accesible = acc_ip()
    if request.environ.get("HTTP_X_FORWARDED_FOR") == None:
        ip = request.environ["REMOTE_ADDR"]
    else:
        ip = request.environ["HTTP_X_FORWARDED_FOR"]
    if passwr == "uywoaNdqoap12Jd01djls" and ip not in accesible:
        with open(path.join(basedir, "Accesable_IP.txt"), "a") as fl:
            fl.write(f",{ip}")

    if ip in accesible:
        id = cypter.decryptIT(request.args.get("id"))
        if id == None:
            return jsonify(status_code=400, message="bad request"), 400
        if connect.select_user(id) != []:
            if date not in connect.list_column():
                connect.new_column(date)
            connect.precence(id, date)
            connect.session.commit()
            connect.session.close()
            return jsonify(status_code=200, message="success"), 200
        else:
            return jsonify(status_code=400, message="bad request"), 400
    else:
        return jsonify(status_code=403, message="forbidden"), 403


@app.errorhandler(404)
def not_found_error(error):
    return jsonify(status_code=404, message="not found"), 404


if __name__ == "__main__":
    app.run(debug=True)

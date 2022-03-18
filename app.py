from db_connect import Database
from flask import Flask, request, render_template
from datetime import datetime
import cypter

app = Flask(__name__)
app.config.update(TESTING=False, DATABASE="user_database.db")


def acc_ip():
    with open("Accesable_IP.txt", "r") as fl:
        accesible = fl.read().split(",")
    return accesible


@app.route("/")
def index():
    date = str(datetime.now()).split(" ")[0].replace("-", "_")
    accesible = acc_ip()
    connect = Database(app.config["DATABASE"])
    passwr = request.args.get("ert426ip")

    if request.environ.get("HTTP_X_FORWARDED_FOR") is None:
        ip = request.environ["REMOTE_ADDR"]
    else:
        ip = request.environ["HTTP_X_FORWARDED_FOR"]

    if passwr == "uywoaNdqoap12Jd01djls" and ip not in accesible:
        with open("Accesable_IP.txt", "a") as fl:
            fl.write(f",{ip}")

    if ip in accesible:
        id = cypter.decryptIT(request.args.get("id"))
        if id == None:
            return render_template("Bad-Format.html"), 400
        if connect.select_user(id) != []:
            if date not in connect.list_column():
                connect.new_column(date)
            connect.precence(id, date)
            connect.db.commit()
            connect.db.close()
            return render_template("200-OK.html"), 200
        else:
            return render_template("Bad-Format.html"), 400
    else:
        return render_template("403-Forbidden.html"), 403


if __name__ == "__main__":
    app.run(debug=True)

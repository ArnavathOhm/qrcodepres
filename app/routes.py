from . import app, cypter
from .models import User, get_db_items, get_db_columns, precence
from .db_to_xlsx import create_db_xlsx
from flask import request, jsonify, send_file
from flask_admin import AdminIndexView, expose
from flask_table import create_table, Col, LinkCol
from threading import Thread
from time import sleep
import os


basedir = os.path.abspath(os.path.dirname(__file__))


# def acc_ip():
#     with open(os.path.join(basedir, "Accesable_IP.txt"), "r") as fl:
#         accesible = fl.read().split(",")
#     return accesible


@app.route("/")
def index():
    # date = str(datetime.now()).split(" ")[0].replace("-", "_")
    # connect = Database(app.config["DATABASE_URL"])

    # # Securing api with ip address
    # passwr = request.args.get("ert426ip")
    # accesible = acc_ip()
    # if request.environ.get("HTTP_X_FORWARDED_FOR") == None:
    #     ip = request.environ["REMOTE_ADDR"]
    # else:
    #     ip = request.environ["HTTP_X_FORWARDED_FOR"]
    # if passwr == "uywoaNdqoap12Jd01djls" and ip not in accesible:
    #     with open(os.path.join(basedir, "Accesable_IP.txt"), "a") as fl:
    #         fl.write(f",{ip}")

    # if ip in accesible:
    id = cypter.decryptIT(request.args.get("id"))
    if id == None:
        return jsonify(status_code=400, message="bad request"), 400
    user = User.query.get_or_404(id)
    precence(user)
    return jsonify(status_code=200, message="success"), 200
    # else:
    #     return jsonify(status_code=403, message="forbidden"), 403


class IndexHomeView(AdminIndexView):
    @expose("/")
    def index(self):
        items = get_db_items()
        PresenceTable = create_table("PresenceTable")
        for col_name in get_db_columns():
            PresenceTable.add_column(col_name, Col(col_name))
        PresenceTable.add_column(
            "edit",
            LinkCol(
                "Edit",
                "user.edit_view",
                url_kwargs=dict(id="id"),
                url_kwargs_extra=dict(url="/admin"),
            ),
        )
        table = PresenceTable(items)
        table.border = True
        return self.render("admin/index.html", table=table)


def delete_file(filename):
    sleep(3)
    os.remove(filename)


@app.route("/download_xlsx")
def download_xlsx():
    filename = os.path.join(basedir, "Presence.xlsx")
    create_db_xlsx(filename)
    Thread(target=delete_file, args=[filename]).start()
    return send_file(filename)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify(status_code=404, message="not found"), 404

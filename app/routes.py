from . import app, cypter
from .models import get_db_items, get_db_columns
from flask import request, jsonify
from flask_admin import AdminIndexView, expose
from flask_table import create_table, Col, LinkCol
from datetime import datetime
from os import path


basedir = path.abspath(path.dirname(__file__))


def acc_ip():
    with open(path.join(basedir, "Accesable_IP.txt"), "r") as fl:
        accesible = fl.read().split(",")
    return accesible


@app.route("/")
def index():
    return "works"
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
    #     with open(path.join(basedir, "Accesable_IP.txt"), "a") as fl:
    #         fl.write(f",{ip}")

    # if ip in accesible:
    #     id = cypter.decryptIT(request.args.get("id"))
    #     if id == None:
    #         return jsonify(status_code=400, message="bad request"), 400
    #     if connect.select_user(id) != []:
    #         if date not in connect.list_column():
    #             connect.new_column(date)
    #         connect.precence(id, date)
    #         connect.session.commit()
    #         connect.session.close()
    #         return jsonify(status_code=200, message="success"), 200
    #     else:
    #         return jsonify(status_code=400, message="bad request"), 400
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


@app.errorhandler(404)
def not_found_error(error):
    return jsonify(status_code=404, message="not found"), 404

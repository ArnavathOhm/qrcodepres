from . import app, db
from .models import User, Date
from .routes import IndexHomeView
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app, name="qrcodepres", template_mode="bootstrap4", index_view=IndexHomeView())
admin.add_view(ModelView(User, db.session, endpoint="user", name="User"))
admin.add_view(ModelView(Date, db.session, name="Date"))

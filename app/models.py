from . import db

dates = db.Table(
    "dates",
    db.Column("date_id", db.Integer, db.ForeignKey("date.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    dates = db.relationship(
        "Date", secondary=dates, lazy="subquery", backref=db.backref("users", lazy=True)
    )

    def __repr__(self) -> str:
        return f"<User: {self.username}, id: {self.id}>"


class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True, unique=True)

    def __repr__(self) -> str:
        return f"<Date: {self.date}>"


def get_db_items():
    res = list()
    for user in User.query.all():
        presence = dict()
        presence.update({"id": user.id, "username": user.username})
        for date in Date.query.all():
            if date not in user.dates:
                presence.update({date.date.strftime("%Y-%m-%d"): "absent"})
            else:
                presence.update({date.date.strftime("%Y-%m-%d"): "present"})
        res.append(presence)
    return res


def get_db_columns():
    res = ["id", "username"]
    for date in Date.query.all():
        res.append(date.date.strftime("%Y-%m-%d"))
    return res

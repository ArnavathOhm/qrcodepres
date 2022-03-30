from db_connect import Database


db = Database("sqlite://")
db.create()


def get_all():
    return db.session.execute("select * from user").all()


def test_list_column():
    assert db.list_column() == ["user_id", "user_name"]


def test_add_user():
    db.add_user(1, "test")
    assert get_all() == [(1, "test")]
    db.session.commit()


def test_rollback():
    db.add_user(2, "test")
    assert get_all() == [(1, "test"), (2, "test")]
    db.session.rollback()
    assert get_all() == [(1, "test")]


def test_new_column():
    db.new_column("precence")
    assert db.list_column() == ["user_id", "user_name", "precence"]


def test_precence():
    # this test automatically tests update method
    db.precence(1, "precence")
    assert get_all() == [(1, "test", "attend")]


def test_select_user():
    db.select_user(1) == [(2, "test", "attend")]

from app.models import User, Date
import json

users = User.query.all()
dates = Date.query.all()

# {user: {date1: -, date2: attend}}

res = dict()
for User in users:
    presence = dict()
    for Date in dates:
        if Date not in User.dates:
            presence.update({Date.date.strftime("%Y-%m-%d"): None})
        else:
            presence.update({Date.date.strftime("%Y-%m-%d"): "attend"})

    res.update({User.username: presence})
print("ALL USER\n")
print(json.dumps(res, indent=2))
print("\n\n")

# specified date
res = dict()
for Date in dates:
    presence = dict()
    for User in users:
        if User not in Date.users:
            presence.update({User.username: None})
        else:
            presence.update({User.username: "attend"})
    res.update({Date.date.strftime("%Y-%m-%d"): presence})
print("ALL DATE\n")
print(json.dumps(res, indent=2))


res = list()
for User in users:
    presence = dict()
    presence.update({"username": User.username})
    for Date in dates:
        if Date not in User.dates:
            presence.update({Date.date.strftime("%Y-%m-%d"): None})
        else:
            presence.update({Date.date.strftime("%Y-%m-%d"): "attend"})

    res.append(presence)

print("TABLE\n")
print(json.dumps(res, indent=2))
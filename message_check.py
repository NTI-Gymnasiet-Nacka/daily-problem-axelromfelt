import sqlite3
from datetime import datetime as dt

# def get_db():

#     db = sqlite3.connect(
#         "./instance/flaskr.sqlite",
#         detect_types=sqlite3.PARSE_DECLTYPES
#     )
#     db.row_factory = sqlite3.Row

#     return db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()


db = sqlite3.connect(
    "./instance/flaskr.sqlite",
    detect_types=sqlite3.PARSE_DECLTYPES
).cursor()

fake_user = db.execute('SELECT username FROM user WHERE id = 1').fetchone()
db.execute('') commit

date = dt.now().strftime('%Y-%m-%d')
time = dt.now().strftime('%H:%M')

posts = db.execute(
    'SELECT * FROM post WHERE date = ? and time = ?', (date, time)).fetchall()
print(posts)
if posts is not None or posts != []:
    users = {}

    for post in posts:
        user = post[1]
        if user not in users.keys():
            users[user] = db.execute(
                'SELECT token FROM user WHERE username = ?', (user,)).fetchone()
print(users)

db.close()

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
date = dt.now().strftime('%Y-%m-%d')
time = dt.now().strftime('%H:%M')

post = db.execute(
    f'SELECT * FROM post WHERE date = ? and time = ?', (date, time)).fetchall()
print(post)
db.close()

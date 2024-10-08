import sqlite3


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
)
db.row_factory = sqlite3.Row
user = db.execute('SELECT * FROM user').fetchall()
print(user)
db.close()

import sqlite3
from datetime import datetime as dt
from push_message import push_message


def check_messages():
    """checks the database if there are any messages that should get pushed. Picks messages according to the date and time written in the database

    """
    date = dt.now().strftime('%Y-%m-%d')
    time = dt.now().strftime('%H:%M')

    db = sqlite3.connect(
        "./instance/flaskr.sqlite",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    cursor = db.cursor()

    posts = cursor.execute(
        'SELECT * FROM post WHERE date = ? and time = ?', (date, time)).fetchall()

    if posts is not None or posts != []:
        user_tokens = {}

        for post in posts:
            user = post[1]
            if user not in user_tokens.keys():
                user_tokens[user] = cursor.execute(
                    'SELECT token FROM user WHERE username = ?', (user,)).fetchone()[0]
            push_message(post[4], user_tokens[user])
            cursor.execute("DELETE FROM post WHERE id = ?", (post[0],))
            db.commit()

    cursor.close()

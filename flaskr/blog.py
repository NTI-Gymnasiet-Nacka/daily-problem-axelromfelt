from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from datetime import datetime as dt
from flaskr.auth import login_required
from flaskr.db import get_db

from push_message import push_message

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()

    if g.user is not None:
        return redirect(url_for('blog.user', username=g.user["username"]))
    else:
        return redirect(url_for('auth.login'))


@bp.route('/user/<username>', methods=('GET', 'POST'))
@login_required
def user(username):
    if g.user['token'] is None:
        if request.method == 'POST':
            token_check = change_token(request.form['token'])
            if token_check is not None:
                flash(token_check)
            else:
                return render_template('blog/user.html')

        return render_template('blog/no_token.html')

    if request.method == 'POST':
        time = request.form['time']
        body = request.form['body']
        date = request.form['date']

        error = None

        if dt.strptime(f'{date} {time}', '%Y-%m-%d %H:%M') <= dt.now():
            error = "Date/time has already passed"

        if not body:
            error = 'Message is required.'

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (time, date, body, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (time, date, body, g.user['username'])
            )
            db.commit()
            flash('Reminder set')
            return redirect(url_for('blog.index'))

    return render_template('blog/user.html')


def change_token(user_token):
    if push_message('setup test', user_token) == 200:
        db = get_db()
        db.execute(
            "UPDATE user SET token = ? WHERE id = ?", (
                user_token, g.user["id"])
        )
        db.commit()
        return None
    else:
        return 'Not a valid user key'

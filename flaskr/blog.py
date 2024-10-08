from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

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
    if request.method == 'POST':
        time = request.form['time']
        body = request.form['body']
        date = False
        if 'type' in request.form.keys():
            date = True

        # print(time_type)
        error = None

        if not time:
            error = 'Time/date is required.'
        elif not body:
            error = 'Message is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (time, body, g.user['username'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/user.html')

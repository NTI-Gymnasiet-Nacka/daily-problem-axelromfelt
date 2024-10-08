from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.auth import login_required
from flaskr.db import get_db

from push_message import push_message

bp = Blueprint('config', __name__, url_prefix='/settings')


@bp.route("/", methods=('GET', 'POST'))
def settings():

    if request.method == 'POST':
        action = request.form["type"]

        if action == 'token':
            if change_token(request.form["token"]) is not True:
                flash("New token is faulty")
        elif action == 'password':
            if not check_password_hash(g.user['password'], request.form["old_password"]):
                flash('Old password does not match')
            elif request.form["new_password"] != request.form["confirm_password"]:
                flash('New passwords does not match')
            else:
                db = get_db()
                db.execute(
                    "UPDATE user SET token = ? WHERE id = ?", (
                        title, body, g.user["id"])
                )
                db.commit()

        else:
            return redirect(url_for('blog.user', username=g.user["username"]))
    if g.user is not None:
        return render_template('config/settings.html')
    else:
        return redirect(url_for('auth.login'))


# @bp.route("/update_token", methods=('POST',))
def change_token(user_token):
    if push_message('setup test', user_token) == 200:
        db = get_db()
        db.execute(
            "UPDATE user SET token = ? WHERE id = ?", (
                user_token, g.user["id"])
        )
        db.commit()
        return True
    else:
        False


def change_password(old_password, new_password, confirm_password):
    if push_message('setup test', user_token) == 200:
        db = get_db()
        db.execute(
            "UPDATE user SET token = ? WHERE id = ?", (
                user_token, g.user["id"])
        )
        db.commit()
        return True
    else:
        False

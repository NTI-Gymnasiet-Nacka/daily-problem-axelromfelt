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
            token_change_result = change_token(request.form["token"])
            flash(token_change_result)

        elif action == 'password':
            password_change_result = change_password(
                request.form["old_password"], request.form["new_password"], request.form["confirm_password"])

            flash(password_change_result)
        elif action == 'username':
            username_change_result = change_username(request.form["username"])
            flash(username_change_result)

        else:
            return redirect(url_for('blog.user', username=g.user["username"]))

    if g.user is not None:
        return render_template('config/settings.html')

    else:
        return redirect(url_for('auth.login'))


def change_token(user_token):
    """takes the users inputen pushover user key and checks if it is correct then returns a message depending on the succes

    Args:
        user_token (str): a pushover user key that is to be checked if it is correct

    Returns:
        str: a message that returns if the token change was succesfull or not
    """
    if push_message('setup test', user_token) == 200:
        db = get_db()
        db.execute(
            "UPDATE user SET token = ? WHERE id = ?", (
                user_token, g.user["id"])
        )
        db.commit()
        return "Token was updated"
    else:
        return "Token was faulty"


def change_password(old_password, new_password, confirm_password):
    """_summary_

    Args:
        old_password (str): users old password
        new_password (str): users new password
        confirm_password (str): users new password enter again to check that they spelled it right

    Returns:
        str: an error message
    """
    if check_password_hash(g.user['password'], old_password):
        if new_password == confirm_password:
            db = get_db()
            db.execute(
                "UPDATE user SET password = ? WHERE id = ?", (
                    generate_password_hash(new_password), g.user["id"],)
            )
            db.commit()
            return "Password was updated"
        return "New passwords does not match"
    else:
        return "Old password is not correct"


def change_username(new_username):
    db = get_db()
    try:
        db.execute(
            "UPDATE user SET username = ? WHERE id = ?",
            (new_username, g.user["id"],),
        )
        db.commit()
    except db.IntegrityError:
        return f"Username {new_username} is already taken"
    return "Username has been updated"

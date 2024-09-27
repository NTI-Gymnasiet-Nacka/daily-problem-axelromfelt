from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('config', __name__, url_prefix='/settings')


@bp.route("/", methods=('GET', 'POST'))
def settings(**kwargs):
    update = kwargs.get('update', None)
    if request.method == 'POST':
        print(update)
        if update == "token":
            print("0")
        else:
            return redirect(url_for('blog.user', username=g.user["username"]))
    if g.user is not None:
        return render_template('config/settings.html')
    else:
        return redirect(url_for('auth.login'))

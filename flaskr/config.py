from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('config', __name__, url_prefix='/settings')


@bp.route("/", methods=('GET', 'POST'))
def settings():
    if request.method == 'POST':
        return redirect(url_for('blog.user', username=g.user["username"]))
    if g.user is not None:
        return render_template('config/settings.html')
    else:
        return redirect(url_for('auth.login'))

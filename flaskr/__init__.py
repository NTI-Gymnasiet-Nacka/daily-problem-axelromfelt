import os

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from message_check import check_messages


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import config
    app.register_blueprint(config.bp)

    scheduler = BackgroundScheduler()
    scheduler.start()

    # Schedule your task
    scheduler.add_job(check_messages, 'interval', minutes=1, coalesce=True)

    return app

# flask --app flaskr run --debug
# flask --app flaskr run --host=0.0.0.0
# flask --app flaskr init-db

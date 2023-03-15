from flask import Flask
from .model import User
app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = 'ajsfbkaefhaefihajf'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

from flask import Flask

app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = 'ajsfbkaefhaefihajf'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

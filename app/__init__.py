from flask import Flask
from api.users import users
from api.items import items
from api.carts import carts


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(users, url_prefix='/api/users')
    app.register_blueprint(items, url_prefix='/api/items')
    app.register_blueprint(carts, url_prefix='/api/carts')


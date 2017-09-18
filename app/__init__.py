from flask import Flask
from .api.users import users
from .api.groups import groups
from .api.posts import posts
from .models import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(users, url_prefix='/api/users')
    app.register_blueprint(groups, url_prefix='/api/groups')
    app.register_blueprint(posts, url_prefix='/api/posts')
    db.init_app(app)


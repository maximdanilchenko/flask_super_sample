from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    subscribers = db.relationship('Subscribers', backref='user', lazy='dynamic')
    posts = db.relationship('Posts', backref='author', lazy='dynamic')


class Subscribers(db.Model):
    subscriber_id
    user_id



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(128)
    text = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    tags


posts_tags


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)


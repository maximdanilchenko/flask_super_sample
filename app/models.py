from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id
    login
    password
    friends


class Groups(db.Model):
    id
    name
    description
    users


class Posts(db.Model):
    id
    name
    text
    tags


posts_tags


class Tags(db.Model):
    id
    name


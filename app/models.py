from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(128)
    text = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    tags = db.relationship('Tags',
                           secondary=posts_tags,
                           backref=db.backref('posts', lazy='dynamic'))


posts_tags = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    posts = db.relationship('Posts',
                            secondary=posts_tags,
                            backref=db.backref('tags', lazy='dynamic'))


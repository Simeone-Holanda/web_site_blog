from sqlalchemy.orm import backref
from sqlalchemy.sql.expression import null
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    print('Ola')
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    username = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now()) # pegando o fusu horario e a data atual do sistema
    # passa o User como referencia sendo user e se todos os posts for apagados esse campo fica vazio
    posts = db.relationship('Post', backref='user', passive_deletes=True)  
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes =  db.relationship('Like', backref='user', passive_deletes=True)
   

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False) # garantindo que o campo n vai está vazio
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    # não pode ser vazio e se o usuario for apagado é apagado todos os posts dele 
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes =  db.relationship('Like', backref='post', passive_deletes=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',ondelete="CASCADE"),nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',ondelete="CASCADE"),nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)

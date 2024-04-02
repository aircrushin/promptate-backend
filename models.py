# database.py
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyWord = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    detail = db.Column(db.String(200), nullable=False)
    useTime = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    varNum = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'keyWord': self.keyWord,
            'type': self.type,
            'detail': self.detail,
            'useTime': self.useTime,
            'color': self.color,
            'varNum': self.varNum
        }

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin
        }
class CommunityData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(255))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)  
    type = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'src': self.src,
            'title': self.title,
            'content': self.content,
            'type': self.type
        }
    
class ShareData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(255))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)  
    type = db.Column(db.String(80), nullable=False)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    createUser = db.Column(db.String(20), default="henry123")

    def to_dict(self):
        return {
            'id': self.id,
            'src': self.src,
            'title': self.title,
            'content': self.content,
            'type': self.type,
            'createTime': self.createTime,
            'createUser': self.createUser
        }
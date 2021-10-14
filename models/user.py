from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_digest = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    orders = db.relationship("Order", cascade="all",
                             backref=db.backref('my_orders', lazy=True))

    def __init__(self, name, address, email, password_digest):
        self.name = name
        self.address = address
        self.email = email
        self.password_digest = password_digest

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "password_digest": self.password_digest,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        allUsers = User.query.all()
        return [user.json() for user in allUsers]

    @classmethod
    def find_by_id(cls, user_id):
        return User.query.filter_by(id=user_id).first()

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

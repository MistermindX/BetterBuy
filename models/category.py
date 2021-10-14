from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    item = db.relationship("Item", backref=db.backref(
        'items_category', cascade="all", lazy=True))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        allCategories = Category.query.all()
        return [category.json() for category in allCategories]

    @classmethod
    def find_by_id(cls, category_id):
        return Category.query.filter_by(id=category_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

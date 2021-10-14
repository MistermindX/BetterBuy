from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    category = db.relationship(
        "Category", backref=db.backref('categories', cascade="all", lazy=True))
    item = db.relationship(
        "OrderItem", backref=db.backref('this_order_items', lazy=True))

    def __init__(self, name, category_id, description):
        self.name = name
        self.category_id = category_id
        self.description = description

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "category_id": self.category_id,
            "description": self.description,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        allItems = Item.query.all()
        return [item.json() for item in allItems]

    @classmethod
    def find_by_id(cls, item_id):
        return Item.query.filter_by(id=item_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

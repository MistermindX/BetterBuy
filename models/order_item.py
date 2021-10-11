from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    color_choice_id = db.Column(db.Integer, db.ForeignKey(
        'color_choice.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    item = db.relationship("Item", backref=db.backref('items', lazy=True))
    color_choice = db.relationship(
        "ColorChoice", backref=db.backref('color_choices', lazy=True))
    order = db.relationship("Order", backref=db.backref('orders', lazy=True))

    def __init__(self, item_id, color_choice_id, order_id, quantity):
        self.item_id = item_id
        self.color_choice_id = color_choice_id
        self.order_id = order_id
        self.quantity = quantity

    def json(self):
        return {
            "id": self.id,
            "item_id": self.item_id,
            "color_choice_id": self.color_choice_id,
            "order_id": self.order_id,
            "quantity": self.quantity,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    @classmethod
    def find_all(cls):
        allOrderedItems = OrderItem.query.all()
        return [items.json() for items in allOrderedItems]

    @classmethod
    def find_by_id(cls, order_item_id):
        return OrderItem.query.filter_by(id=order_item_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

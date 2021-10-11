from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', nullable=False))
    store_location_id = db.Column(db.Integer, db.ForeignKey(
        'store_locations.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    user = db.relationship("User", backref=db.backref('users', lazy=True))
    store_location = db.relationship(
        "StoreLocation", backref=db.backref('store_locations', lazy=True))

    def __init__(self, user_id, store_location_id):
        self.user_id = user_id
        self.store_location_id = store_location_id

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "store_location_id": self.store_location_id,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    @classmethod
    def find_all(cls):
        allOrders = Order.query.all()
        return [order.json() for order in allOrders]

    @classmethod
    def find_by_id(cls, order_id):
        return Order.query.filter_by(id=order_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

from datetime import datetime
from sqlalchemy.orm import backref
from models.db import db


class StoreLocation(db.Model):
    __tablename__ = 'store_locations'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)
    orders = db.relationship("Order", cascade="all",
                             backref=db.backref('orders', lazy=True))

    def __init__(self, address):
        self.address = address

    def json(self):
        return {
            "id": self.id,
            "address": self.address,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        allStores = StoreLocation.query.all()
        return [store.json() for store in allStores]

    @classmethod
    def find_by_id(cls, store_location_id):
        return StoreLocation.query.filter_by(id=store_location_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

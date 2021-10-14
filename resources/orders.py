from flask import request
from flask_restful import Resource
from models.db import db
from sqlalchemy.orm import joinedload
from models.order import Order


class AllOrders(Resource):
    def get(self):
        orders = Order.query.options(joinedload('user', 'order_items')).all()
        return [order.json() for order in orders]

    def post(self):
        data = request.get_json()
        order = Order(**data)
        order.create()
        return order.json(), 201


class OrderDetail(Resource):
    def get(self, order_id):
        order = Order.query.options(joinedload(
            'user', 'order_items')).filter_by(id=order_id).first()
        return order.json()

    def put(self, order_id):
        data = request.get_json()
        order = Order.find_by_id(order_id)
        for key in data:
            setattr(order, key, data[key])
        db.session.commit()
        return order.json()

    def delete(self, order_id):
        order = Order.find_by_id(order_id)
        if not order:
            return {"msg": "Post not found"}, 404
        db.session.delete(order)
        db.session.commit()
        return {"msg": "Post Deleted", "payload": order_id}


class OrderByUser(Resource):
    def get(self, user_id):
        order = Order.query.options(joinedload(
            'user', 'order_items')).filter_by(user_id=user_id).first()
        return order.json()


class ItemsInOrder(Resource):
    def get(self, order_id):
        order = Order.query.options(joinedload(
            'user', 'order_items')).filter_by(id=order_id).first()
        items = [item.json() for item in order.order_items]
        return {**order.json(), "items": items}

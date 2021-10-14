from flask import request
from flask_restful import Resource
from models.db import db
from sqlalchemy.orm import joinedload
from models.order import Order


class AllOrders(Resource):
    def get(self):
        orders = Order.find_all()
        return [order for order in orders]

    def post(self):
        data = request.get_json()
        order = Order(**data)
        order.create()
        return order.json(), 201


class OrderDetail(Resource):
    def get(self, order_id):
        order = Order.query.filter_by(id=order_id).first()
        if not order:
            return {"msg": "Order not found"}, 404
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
        return {"msg": "Order Deleted", "payload": order_id}


class OrderByUser(Resource):
    def get(self, user_id):
        orders = Order.query.options(joinedload(
            'user')).filter_by(user_id=user_id)
        return [order.json() for order in orders]


class ItemsInOrder(Resource):
    def get(self, order_id):
        order = Order.query.options(joinedload(
            'orderitems')).filter_by(id=order_id).first()
        items = [item.json() for item in order.orderitems]
        return {**order.json(), "items": items}

from flask import request
from flask_restful import Resource
from models.db import db
from models.order_item import OrderItem
from sqlalchemy.orm import joinedload


class AllOrderItems(Resource):
    def get(self):
        orderItems = OrderItem.find_all()
        return [orderItem for orderItem in orderItems]

    def post(self):
        data = request.get_json()
        orderItem = OrderItem(**data)
        orderItem.create()
        return orderItem.json(), 201


class OrderItemDetail(Resource):
    def get(self, order_item_id):
        orderItem = OrderItem.query.filter_by(id=order_item_id).first()
        return orderItem.json()

    def put(self, order_item_id):
        data = request.get_json()
        orderItem = OrderItem.find_by_id(order_item_id)
        for key in data:
            setattr(orderItem, key, data[key])
        db.session.commit()
        return orderItem.json()

    def delete(self, order_item_id):
        orderItem = OrderItem.find_by_id(order_item_id)
        if not orderItem:
            return {"msg": "OrderItem not found"}, 404
        db.session.delete(orderItem)
        db.session.commit()
        return {"msg": "Item Deleted", "payload": order_item_id}


class OrderItemItem(Resource):
    def get(self, order_item_id):
        orderItem = OrderItem.query.options(joinedload(
            'item')).filter_by(id=order_item_id).first()
        return orderItem.item.json()

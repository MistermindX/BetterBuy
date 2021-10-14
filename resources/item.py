from flask import request
from flask_restful import Resource
from models.db import db
from models.item import Item
from sqlalchemy.orm import joinedload


class AllItems(Resource):
    def get(self):
        items = Item.find_all()
        return [item for item in items]

    def post(self):
        data = request.get_json()
        item = Item(**data)
        item.create()
        return item.json(), 201


class ItemDetail(Resource):
    def get(self, item_id):
        item = Item.query.filter_by(id=item_id).first()
        return item.json()

    def put(self, item_id):
        data = request.get_json()
        item = Item.find_by_id(item_id)
        for key in data:
            setattr(item, key, data[key])
        db.session.commit()
        return item.json()

    def delete(self, item_id):
        item = Item.find_by_id(item_id)
        if not item:
            return {"msg": "Item not found"}, 404
        db.session.delete(item)
        db.session.commit()
        return {"msg": "Item Deleted", "payload": item_id}

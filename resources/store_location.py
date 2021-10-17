from flask import request
from flask_restful import Resource
from models.db import db
from models.store_locations import StoreLocation


class AllStores(Resource):
    def get(self):
        stores = StoreLocation.find_all()
        return [store for store in stores]

    def post(self):
        data = request.get_json()
        store = StoreLocation(**data)
        store.create()
        return store.json(), 201


class StoreDetail(Resource):
    def get(self, store_id):
        store = StoreLocation.query.filter_by(id=store_id).first()
        if not store:
            return {"msg": "Store not found"}, 404
        return store.json()

    def put(self, store_id):
        data = request.get_json()
        store = StoreLocation.find_by_id(store_id)
        if not store:
            return {"msg": "Store not found"}, 404
        for key in data:
            setattr(store, key, data[key])
        db.session.commit()
        return store.json()

    def delete(self, store_id):
        store = StoreLocation.find_by_id(store_id)
        if not store:
            return {"msg": "Store not found"}, 404
        db.session.delete(store)
        db.session.commit()
        return {"msg": "Category Deleted", "payload": store_id}

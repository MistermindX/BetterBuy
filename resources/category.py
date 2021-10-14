from flask import request
from flask_restful import Resource
from models.db import db
from models.category import Category
from sqlalchemy.orm import joinedload


class AllCategories(Resource):
    def get(self):
        categories = Category.find_all()
        return [category for category in categories]

    def post(self):
        data = request.get_json()
        category = Category(**data)
        category.create()
        return category.json(), 201


class CategoryDetail(Resource):
    def get(self, category_id):
        category = Category.query.filter_by(id=category_id).first()
        if not category:
            return {"msg": "Category not found"}, 404
        return category.json()

    def put(self, category_id):
        data = request.get_json()
        category = Category.find_by_id(category_id)
        if not category:
            return {"msg": "Category not found"}, 404
        for key in data:
            setattr(category, key, data[key])
        db.session.commit()
        return category.json()

    def delete(self, category_id):
        category = Category.find_by_id(category_id)
        if not category:
            return {"msg": "Category not found"}, 404
        db.session.delete(category)
        db.session.commit()
        return {"msg": "Category Deleted", "payload": category_id}


class ItemsByCategory(Resource):
    def get(self, category_id):
        category = Category.query.options(joinedload(
            'categories')).filter_by(id=category_id).first()
        items = [item.json() for item in category.item]
        return {**category.json(), "items": items}

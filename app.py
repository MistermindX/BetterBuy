from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import category, item, order_item, order, user
from resources import auth, category, item, order_item, order
import os

app = Flask(__name__)
CORS(app)
api = Api(app)

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace(
        "://", "ql://", 1)
    app.config['SQLALCHEMY_ECHO'] = False
    app.env = 'production'
else:
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/better_buy'
    app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# Resource Paths Here
api.add_resource(auth.Login, '/users/login')
api.add_resource(auth.Register, '/users/register')

api.add_resource(category.AllCategories, '/categories')
api.add_resource(category.CategoryDetail, '/categories/<int:category_id>')
api.add_resource(category.ItemsByCategory,
                 '/categories/items/<int:category_id>')

api.add_resource(item.AllItems, '/items')
api.add_resource(item.ItemDetail, '/items/id/<int:item_id>')

api.add_resource(order.AllOrders, '/orders')
api.add_resource(order.OrderDetail, '/orders/order/<int:order_id>')
api.add_resource(order.OrderByUser, '/orders/user/<int:user_id>')
api.add_resource(order.ItemsInOrder, '/orders/items/<int:order_id>')

api.add_resource(order_item.AllOrderItems, '/order_items')
api.add_resource(order_item.OrderItemDetail,
                 '/order_items/orderitems/<int:order_item_id>')
api.add_resource(order_item.OrderItemItem,
                 '/order_items/item/<int:order_item_id>')
# Resource Paths Here

if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import category, item, order_item, order, user
from resources import auth, orders

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/better_buy"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# Resource Paths Here
api.add_resource(auth.Login, '/users/login')
api.add_resource(auth.Register, '/users/register')
# Resource Paths Here

if __name__ == '__main__':
    app.run(debug=True)

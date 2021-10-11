from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db

# import models here

# import models here

# import resources here

# import resources here

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/better_buy"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# Resource Paths Here


# Resource Paths Here

if __name__ == '__main__':
    app.run(debug=True)

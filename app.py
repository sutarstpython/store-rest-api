from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,itemlist

app = Flask(__name__)
app.secret_key = 'jose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app,authenticate,identity)       

api.add_resource(Item,'/items/<string:name>')
api.add_resource(itemlist,'/itemlist')
api.add_resource(UserRegister,'/createUser')
 
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
